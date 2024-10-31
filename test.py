import random
from datalist import Cons, Empty, List, bo, concat, foldr, newlist, reverse, take, zipWith,map,filter

# 构建列表的方式
empty : List = Empty() # 构建空列表
list1 : List = newlist(1,2,3,4,5) # 使用函数构建列表
list2 : List = Cons(6,Cons(7,Cons(8,Cons(9,Empty())))) # 直接构建列表
list3 : List = bo(list1,list2) # 将列表拼接成新列表。
list4 : List = newlist(list1,list2) # 构建双层列表。

# 打印列表
print("empty list:",empty)
print("list1:",list1)
print("list2:",list2)
print("list3:",list3)
print("list4:",list4)

# 判断相等性
print("list1 eq list2 is ",list1 == list2)
print("list2 eq list3 is ",list2 == list3)
print("list4 eq list4 is ",list4 == list4)

# 测试concat函数
list5 = concat(list4)
print("list5 is concat(list4):",list5)

# 判断list3与list5相等
print("list3 eq list5 is ",list3 == list5)

# 测试fold函数,测试reverse函数
list1reverse = reverse(list1)
print("list1 reverse is :" ,list1reverse)
print("list1 foldr by (+) ",foldr(lambda x,y:x+y,0,list1))
print("list1 foldl by (+) ",foldr(lambda y,x:x+y,0,list1))

# 测试zipwith
ziplist1 = zipWith(lambda x,y:x+y,list1,list1reverse)
print("zip list1 & it's reverse with (+):",ziplist1)

# 测试take函数
print("take 5 list5 is : ",take(5,list5))

# add two list
print("add list1 and list2:",bo(list1,list2))

# 测试map
print("map list1 plus 1:",map(lambda x:x+1,list1))

# filter
print("filter list5 by ((/= ) ... (%2)):",filter(lambda x:x%2 == 0,list5))

# 算法测试

listrandom : List = newlist(*[random.randint(0,99) for _ in range(100)]) # 注意要转成我们的List
print("show random list",listrandom)

def partition(f,xs):
    def g(x,xss):
        xs,ys = xss
        return (Cons(x,xs),ys) if f(x) else (xs,Cons(x,ys))
    return foldr(g,(Empty(),Empty()),xs)

# partition f xs = foldr (\x,(as,bs) -> if f x then (Cons(x,as),bs) else (as,Cons(x,bs)) ) ([],[]) xs

def qsort(xs):
    match xs:
        case Empty()    : return Empty()
        case Cons(x,xs) :
            left,right = partition(lambda y:y<x,xs)
            return bo(qsort(left),Cons(x,qsort(right)))
        
print("sort listrandom :",qsort(listrandom))