from datalist import *

def filterprimes(ps:List[int]):
    match ps:
        case Empty()    :return Empty()
        case Cons(p,ps) :return Cons(p,filterprimes(filter(lambda x:x%p != 0,ps)))
numbers = newlist(*list(range(2,100)))

print(numbers)

primes = filterprimes(numbers)

print(take(28,primes))

print(take(3,filterprimes(filter(lambda x:x%97 != 0,Cons(98,Cons(99,Empty()))))))

s = take(3,filterprimes(filter(lambda x:x%97 != 0,Cons(98,Cons(99,Empty())))))

match s:
    case Cons(a,Cons(b,xs)) : print(a,b,xs)



def num(x):
    return Cons(x,Thunk(lambda : num(x+1)))

nums = num(1)

print(take(3,nums))

# print(take(2,Cons(1,Empty())))

# print(filter(lambda x:x%2 != 0,numbers))