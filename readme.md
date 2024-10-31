害呀，这里是一个自己定义的列表。

我注意到python的dataclass很像haskell的newtype，于是决定尝试结合python的继承，定义一个类似代数数据类型的List。

类似于haskell的

```haskell
data List a = Empty | Cons a (List a)
```

在这里我们有这样的定义。

```python
class List()
    ...
@dataclass
class Empty(List):
    pass
@dataclass
class Cons(List):
    head:int
    tail:List
```

dataclass让python的类看上去更像代数数据类型了，然后让两个构造函数Empty和Cons继承List。此时List就有了两个构造函数。

根据这个定义我们可以定义更多在List上的操作。比如map、filter、foldr、foldl

在test.py中我们测试了所有的这些函数。此外还尝试了一个算法题，快速排序。事实证明这个运作的也是很不错的。