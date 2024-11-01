from dataclasses import dataclass
from functools import reduce

class List():
    def __init__(self):
        # 想到个事，既然List当且仅当通过Empty和Cons实例化，那么List这个类本身应该给它堵住才对。
        raise TypeError("Cannot instantiate this class directly, only inherit.")
    def __str__(self) -> str:
        s:str = "["
        match self:
            case Empty()         : s = s + "]"
            case Cons(x,Empty()) : s = s + "{}".format(x) + "]"
            case Cons(x,xs)      : s = s + "{},".format(x) + xs.__str__()[1:]
        return s
    def __eq__(self, value: object) -> bool:
        match (self,value):
            case (Empty(),Empty())                 : return True
            case (Cons(x,xs),Cons(y,ys)) if x == y : return xs.__eq__(ys)
            case _                                 : return False
    def __iter__(self):
        self.next = self
        return self
    def __next__(self) -> any:
        match self.next:
            case Empty()   : 
                StopIteration
            case Cons(x,xs): 
                self.next = xs
                return x
@dataclass
class Empty(List):
    pass
@dataclass
class Cons(List):
    head:int # 其实如果升级到3.12可以加入泛型，不过python的事感觉没必要纠结太多,类型标注根本挡不住任何人。
    tail:List

def newlist(*args) -> List:
    return reduce((lambda xs,x: Cons(x,xs)),reversed(args),Empty())

def foldr(f,e,xs:List):
    match(f,e,xs):
        case (_,e,Empty())    : return e
        case (f,e,Cons(x,xs)) : return f(x,foldr(f,e,xs))

def foldl(f,e,xs:List):
    match (f,e,xs):
        case (_,e,Empty())    : return e
        case (f,e,Cons(x,xs)) : return foldl(f,f(e,x),xs)

def zipWith(f,xs:List,ys:List) -> List:
    match (xs,ys):
        case (Empty(),_)            : return Empty()
        case (_,Empty())            : return Empty()
        case (Cons(x,xs),Cons(y,ys)): return Cons(f(x,y),zipWith(f,xs,ys))

def take(n:int,list) -> List:
    match (n,list):
        case (0,xs)         :return Empty()
        case (_,Empty())    :return Empty()
        case (n,Cons(x,xs)) :return Cons(x,take(n-1,xs)) 

def bo(xs:List,ys:List) -> List:
    match (xs,ys):
        case (Empty(),ys)        : return ys
        case (xs,Empty())        : return xs
        case (Cons(x,Empty()),ys): return Cons(x,ys) # 这一条可以省略
        case (Cons(x,xs),ys)     : return Cons(x,bo(xs,ys))

def concat(xss:List) -> List:
    match xss:
        case Empty()      : return Empty()
        case Cons(xs,xss) : return bo(xs,concat(xss))

def reverse(xs:List) -> List:
    return foldl(lambda xs,x:Cons(x,xs),Empty(),xs)

def map(f,xs:List) -> List:
    return foldr(lambda x,xs: Cons(f(x),xs),Empty(),xs)

def filter(f,xs:List) -> List:
    return foldr(lambda x,xs: Cons(x,xs) if f(x) else xs,Empty(),xs)

# 还应该写一个从List还原到list的函数。
# 然后把partition和qsort挪过来。
# 应该对照着再看看Prelude和Data.List里还有啥内容。试着丢进来。
# 还没有尝试过，python能做到类似惰性求值的效果吗？以后试试看。

if __name__ == "__main__" :
    pass