import heapq
# heappush, heappop, heapify, nlargest, nsmallest 
#向堆中插入元素，heapq会维护列表heap中的元素保持堆的性质
heap = []
heapq.heappush(heap, item)
#heapq把列表x转换成堆
heapq.heapify(x)
#从可迭代的迭代器中返回最大的n个数，可以指定比较的key
heapq.nlargest(n, iterable[, key])
#从可迭代的迭代器中返回最小的n个数，可以指定比较的key
heapq.nsmallest(n, iterable[, key])
#从堆中删除元素，返回值是堆中最小或者最大的元素
heapq.heappop(heap)

#pq, cmp
# Q.PriorityQueue(); put(x), empty(), get()
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class Skill(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    #下面两个方法重写一个就可以了
    def __lt__(self,other):#operator < 
        return self.priority < other.priority
    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.priority,other.priority)
    def __str__(self):
        return '(' + str(self.priority)+',\'' + self.description + '\')'

def PriorityQueue_class():
    que = Q.PriorityQueue()
    skill5 = Skill(5,'proficient')
    skill6 = Skill(6,'proficient6')
    que.put(skill6)
    que.put(Skill(5,'proficient'))
    que.put(Skill(10,'expert'))
    que.put(Skill(1,'novice'))
    while not que.empty():
        print (que.get())
while not q.empty():
    next_level = q.get()
    print 'Processing level:', next_level.description


import heapq

heap = [(1, 'one'), (10, 'ten'), (5,'five')]
heapq.heapify(heap)
for x in heap:
	print x,
print

heap[1] = (9, 'nine')
for x in heap:
	print x,