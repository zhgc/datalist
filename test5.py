from datalist import *

# fibs = Thunk(lambda:(Cons(0,Cons(1,zipWith(lambda a,b:a+b,f:=runthunk(fibs),f.tail)))))

# print(take(10,fibs))


def nums(n):
    return Cons(n,Thunk(lambda :nums(n+1)))
numbers = nums(0)
# 一个无穷无尽的自然数集，只取前十项
print(take(10,numbers))

def fib(a,b):
    return Cons(a,Cons(b,Thunk(lambda:fib(c:=a+b,c+b))))
fibs = fib(0,1)
# 一个无穷尽的斐波那契其数列，只取前10项
print(take(10,fibs))

# 在运行前列表的剩余部分以Thunk的形式存在，取值后Thunk消失，求到的值保留下来。