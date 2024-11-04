from dataclasses import dataclass
from functools import reduce
from typing import TypeVar
from type import List,Cons,Empty,Thunk,runthunk

T = TypeVar("T") 
A = TypeVar("A") 

def newlist(*args) -> List:
    return reduce((lambda xs,x: Cons(x,xs)),reversed(args),Empty())

def foldr(f,e,xs:List):
    runthunk(xs)
    match(f,e,xs):
        case (_,e,Empty())    : return e
        case (f,e,Cons(x,xs)) : return f(x,foldr(f,e,xs))

def foldl(f,e,xs:List):
    runthunk(xs)
    match (f,e,xs):
        case (_,e,Empty())    : return e
        case (f,e,Cons(x,xs)) : return foldl(f,f(e,x),xs)

# def foldl_(f,e,xs:List):
#     return foldr(lambda x,xs:f(xs,x),e,reverse_(xs))

# def reverse_(xs:List) -> List:
#     return foldl_(lambda xs,x:Cons(x,xs),Empty(),xs)
# 显然我们不能这样干，用两个函数来回套似乎会引起不好的结果。
# 应该说，其实也可以相互调用，但是要写清楚终止条件。

def zipWith(f,xs:List,ys:List) -> List:
    runthunk(xs)
    runthunk(ys)
    match (xs,ys):
        case (Empty(),_)            : return Empty()
        case (_,Empty())            : return Empty()
        case (Cons(x,xs),Cons(y,ys)): return Cons(f(x,y),zipWith(f,xs,ys))

def take(n:int,list) -> List:
    runthunk(list)
    match (n,list):
        case (0,xs)         :return Empty()
        case (_,Empty())    :return Empty()
        case (n,Cons(x,xs)) :return Cons(x,take(n-1,xs)) 

def bo(xs:List,ys:List) -> List:
    runthunk(xs)
    runthunk(ys)
    match (xs,ys):
        case (Empty(),ys)        : return ys
        case (xs,Empty())        : return xs
        case (Cons(x,Empty()),ys): return Cons(x,ys) # 这一条可以省略
        case (Cons(x,xs),ys)     : return Cons(x,bo(xs,ys))

def concat(xss:List[List[T]]) -> List[T]:
    runthunk(xss)
    match xss:
        case Empty()      : return Empty()
        case Cons(xs,xss) : return bo(xs,concat(xss))

def reverse(xs:List) -> List:
    runthunk(xs)
    return foldl(lambda xs,x:Cons(x,xs),Empty(),xs)

def map(f,xs:List) -> List:
    runthunk(xs)
    return foldr(lambda x,xs: Cons(f(x),xs),Empty(),xs)

def filter(f,xs:List) -> List:
    runthunk(xs)
    return foldr(lambda x,xs: Cons(x,xs) if f(x) else xs,Empty(),xs)

# 还应该写一个从List还原到list的函数。
# 然后把partition和qsort挪过来。
# 应该对照着再看看Prelude和Data.List里还有啥内容。试着丢进来。
# 还没有尝试过，python能做到类似惰性求值的效果吗？以后试试看。

if __name__ == "__main__" :
    list1 : List = newlist(1,2,3,4,5)
    print("list1 foldr",foldr(lambda x,xs:Cons(x,xs),Empty(),list1))
    print("list1 foldl",foldl(lambda xs,x:Cons(x,xs),Empty(),list1))
    # print("list1 foldl_",foldl_(lambda xs,x:Cons(x,xs),Empty(),list1))