from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T") # List 的类型
F = TypeVar("F")
class List(Generic[T]):
    def __init__(self):
        # 想到个事，既然List当且仅当通过Empty和Cons实例化，那么List这个类本身应该给它堵住才对。
        raise TypeError("Cannot instantiate this class directly, only inherit.")
    def __str__(self) -> str:

        # runthunk(self)
        match self:
            case Thunk(xs):
                self = xs()
            case Cons(x,Thunk(xs)):
                self.tail = xs()
        # print函数会避免修改对象，因此runthunk会遇到麻烦，折中的处理是把match直接写在这里。
        # 但是，print的计算结果并不会保留下来。
        s:str = "["
        match self:
            case Empty()          : s = s + "]"
            case Cons(x,Empty())  : s = s + "{}".format(x) + "]"
            case Cons(x,xs)       : s = s + "{},".format(x) + xs.__str__()[1:]
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
        case Cons(x,Thunk(xs)):
            list.tail = xs()
