from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T") # List 的类型
F = TypeVar("F")
class List(Generic[T]):
    def __init__(self):
        # 想到个事，既然List当且仅当通过Empty和Cons实例化，那么List这个类本身应该给它堵住才对。
        raise TypeError("Cannot instantiate this class directly, only inherit.")
    def __str__(self) -> str:
        runthunk(self)
        # runthunk(self) # runthunk两次解决问题。不过怎么解决的我暂时蒙在鼓里。
        s:str = "["
        match self:
            case Empty()          : s = s + "]"
            case Cons(x,Empty())  : s = s + "{}".format(x) + "]"
            case Cons(x,xs)       : s = s + "{},".format(x) + xs.__str__()[1:]
            # case Thunk(_)         : pass 
        return s
    __repr__ = __str__
    def __eq__(self, value: object) -> bool:
        runthunk(self)
        runthunk(value)
        match (self,value):
            case (Empty(),Empty())                 : return True
            case (Cons(x,xs),Cons(y,ys)) if x == y : return xs.__eq__(ys)
            case _                                 : return False
    def __iter__(self):
        self.next = self
        return self
    def __next__(self) -> any:
        runthunk(self)
        match self.next:
            case Empty()   : 
                StopIteration
            case Cons(x,xs): 
                self.next = xs
                return x
# List = TypeVar("List",List_)
@dataclass
class Empty(List):
    pass
@dataclass
class Cons(List):
    head:T 
    tail:List[T]

# 也许应该加一个Thunk，完成惰性列表。

@dataclass
class Thunk(List):
    func:F # () -> List
def runthunk(list):
    match list:
        case Thunk(xs) :
            list = xs()
            runthunk(list)
        case Cons(_,Thunk(xs)):
            list.tail = xs()
            runthunk(list)
        # case _ :pass
