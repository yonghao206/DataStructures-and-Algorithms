# Design



### [146. LRU Cache](https://leetcode-cn.com/problems/lru-cache/)

Difficulty: **中等**

\*\*\*\*

![](../.gitbook/assets/image%20%2810%29.png)

![](../.gitbook/assets/image%20%281%29.png)

**For the get method, we need that the time complexity is O\(1\), we can use hashtable** 

Design and implement a data structure for . It should support the following operations: `get` and `put`.

`get(key)` - Get the value \(will always be positive\) of the key if the key exists in the cache, otherwise return -1.  
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a **positive** capacity.

**Follow up:**  
Could you do both operations in **O\(1\)** time complexity?

**Example:**

```text
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

**Solution**

Language: **Python3**

```python
​class LRUCache:
    def __init__(self, capacity: int):
        self.remain = capacity
        self.dic = collections.OrderedDict()
    # a = [('a', 1), ('b', 2), ('c', 3)]) #正常插入是依次加入左边，pop也是从左边开始，
    # a.move_to_end('a') # OrderedDict([('b', 2), ('c', 3), ('a', 1)])
    # a.popitem(last=False) 先pop出来头节点
    def get(self, key: int) -> int:
        if key in self.dic:
            v = self.dic[key]
            self.dic.move_to_end(key)
            return v 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
        '''Remove and return a (key, value) pair from the dictionary.
        Pairs are returned in LIFO order if last is true or FIFO order if false.
        '''
                self.dic.popitem(last=False)
        self.dic[key] = value 
```







### [460. LFU Cache](https://leetcode-cn.com/problems/lfu-cache/)

Difficulty: **困难**

![](../.gitbook/assets/image%20%286%29.png)

Design and implement a data structure for cache. It should support the following operations: `get` and `put`.

`get(key)` - Get the value \(will always be positive\) of the key if the key exists in the cache, otherwise return -1.  
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie \(i.e., two or more keys that have the same frequency\), the least **recently** used key would be evicted.

Note that the number of times an item is used is the number of calls to the `get` and `put` functions for that item since it was inserted. This number is set to zero when the item is removed.

**Follow up:**  
Could you do both operations in **O\(1\)** time complexity?

**Example:**

```text
LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

**Solution**

Language: **Python3**

```text
​
```

