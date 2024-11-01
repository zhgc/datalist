
class A():
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
    __match_args__ = ("a","b","c")
aa = A(1,2,3)
match aa:
    case A(a,b,c): print(a,b,c)
    case _ : print("nothing")

class B():
    def __init__(self,a,b,c) -> None:
        self.a = c
        self.b = a
        self.c = b
    __match_args__ = ("a","b","c")

bb = B(1,2,3)
match bb:
    case B(a,b,c): print(a,b,c)
    case _ : print("nothing")

class C():
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
    __match_args__ = ("c",)

cc = C(1,2,3)
match cc:
    case C(c): print(c)
    case C(a,b,c): print(a,b,c)
    case _ : print("nothing")