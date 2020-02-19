![1581366574101](D:\markdwonPictures\1581366574101.png)

## 1. Array

### **Palindromic:** 

5最长回文 https://www.youtube.com/watch?v=ZnzvU03HtYk dp可以做

下面这两个图能够很好的分析出来，到底如何遍历的。因为我们要用到什么，然后我们如何遍历

![1580052502997](D:\markdwonPictures\1580052502997.png)

647回文个数 用第五题的dp方法，很快

131返回回文划分,  回溯和dp方法

132返回回文划分II, 

9： 回文数字

125：有效回文

5，516： 二者都是palindrome，一个是subarray(不连续)，一个是substring(连续)dp

![1580095524468](D:\markdwonPictures\1580095524468.png)

![1580095716745](D:\markdwonPictures\1580095716745.png)

![1580098662112](D:\markdwonPictures\1580098662112.png)



**矩阵题目：**

73：矩阵归0，inplace，把第一行第一列当作标记行列

48，54，59：

304：矩阵前缀和



### PrefixSum

对于hashtable的使用和理解是一个很好的组合，subarray一般就涉及到前缀和

1: two sum，下面题目理解的基础

560，523，976对比看

713：双指针

437：对于前缀和在树中的应用，好题目(还涉及部分回溯)

974

53， 152： dp问题一个前缀和一个前缀积题目类似

209: 双指针

304：矩阵前缀和



### 单调栈Monotonous stack

84 85 

### 双指针	

easy:

medium:

hard: 76

### heap

## 2. 树

112, 437：对于前缀和在树中的应用，好题目(还涉及部分回溯)

534, 124, 



### LinkedList

### UninoFind

803 684  685

https://zhuanlan.zhihu.com/p/35395742

### Trie



## 3. DP

![1580659189810](D:\markdwonPictures\1580659189810.png)



### 记忆化搜索递归=>DP

帮助更好的理解动态规划

91：解码方法

![1580605486185](D:\markdwonPictures\1580605486185.png)











打家劫舍: 198, 213, 337

数字类似：343，279，

### 股票系列

![1580335681876](D:\markdwonPictures\1580335681876.png)

![1580335701187](D:\markdwonPictures\1580335701187.png)

题目

**k=1**

![1580335732356](D:\markdwonPictures\1580335732356.png)

这里当i=0时需要特判一下

![1580335986876](D:\markdwonPictures\1580335986876.png)

空间优化

![1580336344381](D:\markdwonPictures\1580336344381.png)

**第二题，k = +infinity**

![1580336715627](D:\markdwonPictures\1580336715627.png)

![1580336759773](D:\markdwonPictures\1580336759773.png)

**第三题，k = +infinity with cooldown**

![1580337167871](D:\markdwonPictures\1580337167871.png)



### LIS LCS

10

![1581403507033](D:\markdwonPictures\1581403507033.png)



![1581349926378](D:\markdwonPictures\1581349926378.png)

72

![1581355674487](D:\markdwonPictures\1581355674487.png)



![1581383906967](D:\markdwonPictures\1581383906967.png)



### knapsack

```python
for i in range(1,n+1):
    for j in range(vi, amount+1):
        d[j] = max(d[j], d[j-v]+wi)
        #	d[i][j] = max(d[i-1][j], d[i][j-v]+wi) #完全背包
        # 完全背包的公式
        # d[i][j] = d[i-1][j]+d[i-1][j-nums[i]] + ... d[i-1][j-x*nums[i]]
        # d[i][j-nums[i]] =   d[i-1][j-nums[i]] + ... d[i-1][j-x*nums[i]]
        # d[i][j] = d[i-1][j]+d[i][j-nums[i]]
        
for i in range(1, n+1):
    for j in range(amount+1, 0, -1):
        d[j] = max(d[j], d[j-v]+wi)
        #d[i][j] = max(d[i-1][j], d[i-1][j-v]+wi) #01背包
	
    #01: d[i][j] = d[i-1][j], d[i-1][j-vi]+wi
    #完全:d[i][j] = d[i-1][j], d[i][j-vi]+wi
# 多重背包
# 多重背包问题的思路跟完全背包的思路非常类似，只是k的取值是有限制的
d[i][v] = max(d[i-1][v-k*c[i]]+w[i] | 0<=k<=n[i])
for i in range(1, n):
    for j in range(1, m):
    	for k in range(1, n):
            if j>=k*v[i] and j<=s[i]: #v体积 w价值
                f[i][j] = max(f[i][j], f[i-1][j-k*v[i]]+k*w[i])
                
```



#### 完全背包

322完全背包求可能的最少纸币数字， 518是完全背包

377和518不是同一个题目，但是有一定的相似度，还是不太理解，以后再看看

518与39类似一个是求解的个数，一个是把所有结果求出来

多重背包

多重背包的经典优化=》二进制优化，对于任意一个s，能够分成,1, 2, 4, ... 2^k, c （即logs份）是的能够构成[0,s]任意一个数字。把 O(NVS)的复杂度优化为 NVlogS![1580766783183](D:\markdwonPictures\1580766783183.png)

### 区间DP

f[L,R]：把这个区间染成最终的样子的方式 **最小值**

属性：max/min/count

从最左边染成什么位置来进行划分

516：[516. Longest Palindromic Subsequence](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)

[664. Strange Printer](https://leetcode-cn.com/problems/strange-printer/)

[730. Count Different Palindromic Subsequences](https://leetcode-cn.com/problems/count-different-palindromic-subsequences/)



## 4. 排序

![1581092094464](D:\markdwonPictures\1581092094464.png)

top down: l1, l2 = split(l) 

```python
l1, l2 = split(l)
l1_1 = sortList(l1)
l2_1 = sortList(l2)
merge(l1_1, l2_1)

```



## 5. 搜索/回溯/BFS/DFS

![1581000170798](D:\markdwonPictures\1581000170798.png)

```python
def solution(self, nums):
    if not nums: return 0
    self.res = []
    self.dfs(nums, 0, []) #参数多传几个
    return self.res 
def dfs(self, nums, idx, unit):
    if idx == len(nums):#base case改一下
        self.res.append(unit[:])
    for i in range(idx, len(nums)):
		# 剪枝条件
        unit.append(nums[i])
        self.dfs(nums, i+1, unit)
        unit.pop()
```



常见疑问

1.  判断什么时候用dp，什么时候用回溯，回溯一般是要具体列表和字符串返回， dp一般求属性值，min/max/count
2.  回溯题目一般时遍历空间解，需要完全遍历空间，一般通过改变idx的值来满足搜索要求
3.  可以通过题目性质，来进行提前的剪枝（if条件约束，提早结束搜索）
4.  参数一遍，题目给的都写上，然后加个idx，level就差不都了。

17, 39, 40, 77, 78, 90, 216

46, 47, 784

```python
if i > idx and nums[i-1] == nums[i]:
    continue

```





## 6 二分

https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/

![1581120155204](D:\markdwonPictures\1581120155204.png)

![1581120333155](D:\markdwonPictures\1581120333155.png)



