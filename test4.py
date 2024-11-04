# 试试看惰性列表能不能用

from datalist import *

tt = Cons(0,Thunk(lambda : Thunk(lambda : Cons(1,Cons(2,Empty())))))

# print(tt.tail.__class__)
print(tt.__str__())
# print(tt.tail.__class__)
print(tt)
# print(tt.tail.__class__)
# print(tt)



# runthunk(tt)
# tt.__str__()


def nums(n):
    return Cons(n,Thunk(lambda :nums(n+1)))

# numbers 一个无穷无尽的自然数序列。
numbers = nums(0)

print(take(3,numbers) == tt)
print(tt.tail.tail.__class__)