from dataclasses import dataclass
from functools import reduce

class List():
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
            case (_,_)                             : return False
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
    head:int # 其实如果升级到3.12可以加入泛型，不过python的事没必要纠结太多。
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
        case (Empty(),Empty())      : return Empty()
        case (_,Empty())            : return Empty()
        case (Empty(),_)            : return Empty()
        case (Cons(x,xs),Cons(y,ys)): return Cons(f(x,y),zipWith(f,xs,ys))

def take(n,list) -> List:
    match (n,list):
        case (0,xs)         :return Empty()
        case (_,Empty())    :return Empty()
        case (n_,Cons(x,xs)):return Cons(x,take(n_-1,xs)) 

def bo(xs:List,ys:List) -> List:
    match (xs,ys):
        case (Empty(),Empty())   : return Empty()
        case (Empty(),ys)        : return ys
        case (xs,Empty())        : return xs
        case (Cons(x,Empty()),ys): return Cons(x,ys)
        case (Cons(x,xs),ys)     : return Cons(x,bo(xs,ys))

def concat(xss:List) -> List:
    match xss:
        case Empty()      : return Empty()
        case Cons(xs,xss) : return bo(xs,concat(xss))

def reverse(xs:List) -> List:
    return foldl(lambda xs,x:Cons(x,xs),Empty(),xs)

def map(f,xs:List) -> List:
    return foldr((lambda x,xs: Cons(f(x),xs)),Empty(),xs)

def filter(f,xs:List) -> List:
    return foldr(lambda x,xs: Cons(x,xs) if f(x) else xs,Empty(),xs)




        

if __name__ == "__main__" :
    l:List = Cons(1,Cons(2,Cons(3,Empty())))
    l2:List = newlist(4,5,6)
    l3:List = Empty()

    match l:
        case Empty()            : print("nothing")
        case Cons(x,Cons(y,xs)) : print(x,y)
        case Cons(x,xs)         : print("head is",x)

    match l2:
        case Empty()            : print("l2 is nothing")
        case Cons(x,Cons(y,xs)) : print(x,y)
        case Cons(x,xs)         : print("l2 head is",x)

    print(take(2,l2))
    print(newlist(1,2,3) == newlist(1,2,3))
    print(newlist(1,2,"3",4))
    ll = newlist(newlist(1,2,3),newlist(4,5,6))
    print(ll)
    print(bo(l,l2))
    l4 = concat(ll)
    print("l4 is ",l4)
    print("reverse l4 is",reverse(l4))
    it = iter(l4)
    print(next(it))
    print(foldr((lambda x,y:x+y),0,l))
    print(map(lambda x:x*x,l4))
    print("l4 filter",filter(lambda x: x % 2 == 0,l4))