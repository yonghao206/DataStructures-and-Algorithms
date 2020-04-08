# DP

## key concepts

top-down with memoization

bottom-up with tabulation

Tabulation is the opposite of the top-down approach and avoids recursion. In this approach, we solve the problem “bottom-up” \(i.e. by solving all the related sub-problems first\). This is typically done by filling up an n-dimensional table. Based on the results in the table, the solution to the top/original problem is then computed.

Tabulation is the opposite of Memoization, as in Memoization we solve the problem and maintain a map of already solved sub-problems. In other words, in memoization, we do it top-down in the sense that we solve the top problem first \(which typically recurses down to solve the sub-problems\).



### [62. Unique Paths](https://leetcode-cn.com/problems/unique-paths/)

Difficulty: **中等**

A robot is located at the top-left corner of a _m_ x _n_ grid \(marked 'Start' in the diagram below\).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid \(marked 'Finish' in the diagram below\).

How many possible unique paths are there?

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)  
Above is a 7 x 3 grid. How many possible unique paths are there?

**Example 1:**

```text
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1\. Right -> Right -> Down
2\. Right -> Down -> Right
3\. Down -> Right -> Right
```

**Example 2:**

```text
Input: m = 7, n = 3
Output: 28
```

**Constraints:**

* `1 <= m, n <= 100`
* It's guaranteed that the answer will be less than or equal to `2 * 10 ^ 9`.

**Solution**

Language: **Python3**

```text
​
```

### [63. Unique Paths II](https://leetcode-cn.com/problems/unique-paths-ii/)

Difficulty: **中等**

A robot is located at the top-left corner of a _m_ x _n_ grid \(marked 'Start' in the diagram below\).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid \(marked 'Finish' in the diagram below\).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

**Note:** _m_ and _n_ will be at most 100.

**Example 1:**

```text
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1\. Right -> Right -> Down -> Down
2\. Down -> Down -> Right -> Right
```

**Solution**

Language: **Python3**

```python
​class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        # 第一排和第一列为1
        d = [[1]*n for i in range(m)]
        d[0][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m-1][n-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0]*(n+1) for _ in range(m+1)]
        d[1][1] = 1
        for i in range(1, m+1):
            for j in range(1,n+1):
                if i==1  and j == 1:
                    continue
                d[i][j] = d[i-1][j]+d[i][j-1]
        return d[m][n]
```

### [63. Unique Paths II](https://leetcode-cn.com/problems/unique-paths-ii/)

Difficulty: **中等**

A robot is located at the top-left corner of a _m_ x _n_ grid \(marked 'Start' in the diagram below\).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid \(marked 'Finish' in the diagram below\).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

**Note:** _m_ and _n_ will be at most 100.

**Example 1:**

```text
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1\. Right -> Right -> Down -> Down
2\. Down -> Down -> Right -> Right
```

**Solution**

Language: **Python3**

```python
​
class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        if not g or not g[0]: return 0 
        n, m = len(g), len(g[0])
        d = [[0]*(m+1) for _ in range(n+1)]
        if g[0][0] == 1:
            return 0
        else:
            d[1][1] = 1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i == 1 and j == 1:
                    continue 
                if g[i-1][j-1] == 1:
                    d[i][j] = 0
                else:
                    d[i][j] = d[i-1][j] + d[i][j-1]
        return d[n][m]
        
class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])
        d = [[0]*m for _ in range(n)]
        if g[0][0]:
            return 0
        else:
            d[0][0] = 1
        for i in range(n):
            for j in range(m):
                if g[i][j]:
                    continue 
                else:
                    if i>0:
                        d[i][j] += d[i-1][j]
                    if j>0:
                        d[i][j] += d[i][j-1]
        return d[n-1][m-1]
```

### 118 119 120三角形

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]*(i+1) for i in range(numRows)]
        # res[i][j] = res[i-1][j-1] + res[i-1][j]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res 
        
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0]*(rowIndex+1)
        for i in range(0, rowIndex+1):
            res[i] = 1 # 填充最后一个位置，并且从后往前遍历
            # 因为当前值由上一层的值对应位置和上一层的前一个值对应的
            for j in range(i-1,0,-1):
                res[j] = res[j-1]+res[j]
        return res 

```

### [120. Triangle](https://leetcode-cn.com/problems/triangle/)

Difficulty: **中等**

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```text
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `11` \(i.e., **2** + **3** + **5** + **1** = 11\).

**Note:**

Bonus point if you are able to do this using only _O_\(_n_\) extra space, where _n_ is the total number of rows in the triangle.

**Solution**

Language: **Python3**

```python
​class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:
        if not nums or not nums[0]: return 0 
        n = len(nums)
        f = [[0]*n for _ in range(2)]
        # f[0][0] = nums[0][0] 自己开辟的空间，不需要
        # 如果在nums上面改，可以从range(1,n)开始
        # f[i][j] = nums[i][j] + min(f[i-1][j], f[i-1][j-1])
        # if j>0 if j<i
        for i in range(n):
            for j in range(i+1):
                if j>0 and j<i:
                    f[i&1][j] = nums[i][j] + min(f[i-1&1][j], f[i-1&1][j-1])
                elif j == 0:
                    f[i&1][j] = nums[i][j] + f[i-1&1][j]
                else:
                    f[i&1][j] = nums[i][j] + f[i-1&1][j-1]
        return min(f[n-1&1])

# 用S:O(n)的最聪明的方法，只需要直接加一个&1
class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:
        n = len(nums)
        f = [[0]*n for i in range(2)]
        f[0][0] = nums[0][0]
        for i in  range(1,n):
            for j in range(i+1):
                if j == 0:
                    f[i&1][j] = f[i-1&1][j] + nums[i][j]
                elif j == i:
                    f[i&1][j] = f[i-1&1][j-1]+nums[i][j]
                else:
                    f[i&1][j] = min(f[i-1&1][j],f[i-1&1][j-1])+nums[i][j]
        # print(f)
        return min(f[n-1&1])
```

### [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

Difficulty: **简单**

给定一个数组，它的第 _i_ 个元素是一支给定股票第 _i_ 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

**示例 1:**

```text
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```

**示例 2:**

```text
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

**Solution**

Language: **Python3**

```python
​# class Solution: 进行一次交易，通过和每个结果与min对比
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices)<=1: return 0
#         minbuyprice = float('inf')
#         maxprofit = 0

#         for price in prices:
#             minbuyprice = min(minbuyprice, price)
#             maxprofit = max(maxprofit, price-minbuyprice)
#         return maxprofit
class Solution: #差分思想
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        maxProfit = 0
        minPrice = float('inf')
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit
```

#### [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

Difficulty: **简单**

给定一个数组，它的第 _i_ 个元素是一支给定股票第 _i_ 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1:**

```text
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
```

**示例 2:**

```text
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

**示例 3:**

```text
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

**Solution**

Language: **Python3**

```python
​# class Solution: #贪心
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         n = len(prices)
#         maxProfit = 0
#         for i in range(1, n):
#             if prices[i]>prices[i-1]:
#                 maxProfit+=prices[i]-prices[i-1]
#         return maxProfit
class Solution: #可以用贪心的也可以用dp来做
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices: return 0
        if len(prices)<2: return 0
        n = len(prices)
        d = [[0]*2 for _ in range(n+1)] # n*2; 
        # [0]没有股票 [1]有股票 d[i][1]前i天持有股票的最大利润
        # d[i][0]前i天持没有有股票的最大利润
        d[0][0] = 0
        # d[0][1] = -prices[0]
        d[0][1] = float('-inf')
        for i in range(1, n+1):
            d[i][0] = max(d[i-1][0], d[i-1][1] + prices[i-1])
            d[i][1] = max(d[i-1][0]-prices[i-1], d[i-1][1])
        # print(d)
        return d[-1][0]
```

### [139. Word Break](https://leetcode-cn.com/problems/word-break/)

Difficulty: **中等**

Given a **non-empty** string _s_ and a dictionary _wordDict_ containing a list of **non-empty** words, determine if _s_ can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.

**Example 1:**

```text
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**

```text
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

**Example 3:**

```text
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

**Solution**

Language: **Python3**

```python
​class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return True 
        n = len(s)
        d = [False]*(n+1)
        d[0]=True 
        w = set(wordDict)
        lengths = list(map(len, wordDict))
        for i in range(1, n+1):
            for length in lengths:
                if i>=length and d[i-length] and s[i-length:i] in w:
                    d[i] = True 
                    break 
        return d[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = [False]*(n+1)
        d[0] = True # d[i]表示s[0:i-1]符合要求，在s里面[0:-1]为空符合 d[1] 为s[0:0]需要测试了
        dic = set(wordDict)
        for i in range(1, n+1):
            for j in  range(i):
                # d[j]表示前j个字符已经拆分成功
                if d[j] and s[j:i] in dic:
                    d[i] = True
                    break
        return d[n]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        self.memo = {}
        for word in wordDict:
            dic[word] = True 
        return self.dfs(s, dic)
    def dfs(self, s, dic) -> bool:
        if not s:return True 
        if s in self.memo:
            return self.memo[s]
        for i in range(1,len(s)+1):
            if s[:i] in dic and self.dfs(s[i:], dic):
                self.memo[s] = True 
                return True 
        self.memo[s] = False 
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        for word in wordDict:
            dic[word] = True 
        self.memo = {}
        self.dfs(s, dic)
        return self.memo[s]

    def dfs(self, s, dic):
        if not s: return True 
        if s in self.memo:
            return self.memo[s]
        for i in range(len(s)):
            # 5: 0,1,2,3,4
            if s[:i+1] in dic and self.dfs(s[i+1:], dic):
                self.memo[s] = True 
                return True 
        self.memo[s] = False 
        return False
```

## 背包问题

![](../.gitbook/assets/image%20%284%29.png)

1. 上面是完全背包和0-1背包的模板，要熟悉并且理解，心中有图
2. 
![](../.gitbook/assets/image%20%283%29.png)

通过最大值与前一个值比较，如果不相等，说明当前元素被使用，我们能够通过一个for循环了解到到底是使用了哪些元素

```python
from __future__ import print_function


def solve_knapsack(profits, weights, capacity):
  # basic checks
  n = len(profits)
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0 for x in range(capacity+1)] for y in range(n)]

  # populate the capacity = 0 columns, with '0' capacity we have '0' profit
  for i in range(0, n):
    dp[i][0] = 0

  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(0, capacity+1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  # process all sub-arrays for all the capacities
  for i in range(1, n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
      # exclude the item
      profit2 = dp[i - 1][c]
      # take maximum
      dp[i][c] = max(profit1, profit2)

  print_selected_elements(dp, weights, profits, capacity)
  # maximum profit will be at the bottom-right corner.
  return dp[n - 1][capacity]

# 打印具体的包括的item
def print_selected_elements(dp, weights, profits, capacity):
  print("Selected weights are: ", end='')
  n = len(weights)
  totalProfit = dp[n-1][capacity]
  for i in range(n-1, 0, -1):
    if totalProfit != dp[i - 1][capacity]:
      print(str(weights[i]) + " ", end='')
      capacity -= weights[i]
      totalProfit -= profits[i]

  if totalProfit != 0:
    print(str(weights[0]) + " ", end='')
  print()


def main():
  print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
  print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()

# 0-1空间优化
def solve_knapsack(profits, weights, capacity):
  # TODO: Write - Your - Code
  # return -1;
  n = len(profits)
  d = [0]*(capacity+1)
  for i in range(n):
    for j in range(capacity, weights[i]-1, -1):
      d[j] = max(d[j], profits[i] + d[j-weights[i]])
  return d[-1]


```





### [416. Partition Equal Subset Sum](https://leetcode-cn.com/problems/partition-equal-subset-sum/)

Difficulty: **中等**

Given a **non-empty** array containing **only positive integers**, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Note:**

1. Each of the array element will not exceed 100.
2. The array size will not exceed 200.

**Example 1:**

```text
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```text
Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
```

**Solution**

Language: **Python3**

```python
​class Solution: # O(n*sum/2) 100万可以在1s内完成计算
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False 
        total = sum(nums)
        if total%2 == 1: return False 
        n = total//2
        # 前i个元素是否可以填满这个背包容量[0,n]
        # =》是否所有的元素能够填充一半的sum，能，则另外一半也等于sum
        memo = [False]*(n+1)
        # 这里相当于我们把第一层的值先赋上
        for i in range(n+1):
            memo[i] = (nums[0] == i) 
        for i in range(1, len(nums)):
            for j in range(n, nums[i]-1, -1):
                memo[j] =( memo[j] or memo[j-nums[i]])
        print(memo)
        return memo[n]


class Solution: # O(n*sum/2) 100万可以在1s内完成计算
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False 
        total = sum(nums)
        if total % 2: return False 
        C = total//2
    
        self.memo = [[-1]*(C+1) for _ in range(len(nums))]
        return bool(self.best(nums, C, len(nums)-1)) #前index的和能够等于C

    # memo[i][c]表示使用索引[0...i]是否可以填充容量为c的背包，没有计算表示-1; 0表示不可以填充; 1表示可以填充
    def best(self, nums, c, index):
        if c == 0: return True 
        if c < 0 or index < 0: return False 
        if self.memo[index][c]!=-1:
            return self.memo[index][c]
        res = self.best(nums, c, index-1) or self.best(nums, c-nums[index], index-1)
        self.memo[index][c] = res 
        return res 

```



### [494. Target Sum](https://leetcode-cn.com/problems/target-sum/)

Difficulty: **中等**

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols `+` and `-`. For each integer, you should choose one from `+` and `-` as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

**Example 1:**

```text
Input: nums is [1, 1, 1, 1, 1], S is 3\. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```

**Note:**

1. The length of the given array is positive and will not exceed 20.
2. The sum of elements in the given array will not exceed 1000.
3. Your output answer is guaranteed to be fitted in a 32-bit integer.

**Solution**

Language: **Python3**

```python
​class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dfs 2^n
        if not nums: return 0
        self.res = 0
        self.S = S 
        self.d = {}
        return self.dfs(nums, 0, 0)
 
    def dfs(self, nums, index, total):
        if (index, total) in self.d:
            return self.d[(index,total)]
        if index == len(nums):
            if total == self.S:
                return 1 
            return 0
        res = 0
        res += self.dfs(nums, index+1, total+nums[index])
        res += self.dfs(nums, index+1, total-nums[index])
        self.d[(index, total)] = res 
        return res 
```

### [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)

Difficulty: **中等**

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 `-1`。

**示例 1:**

```text
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
```

**示例 2:**

```text
输入: coins = [2], amount = 3
输出: -1
```

**说明**:  
你可以认为每种硬币的数量是无限的。

**Solution**

Language: **Python3**

```python
​# # 完全背包的方法 TLE 这里面用的是
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         d = [[float('inf')]*(amount+1) for _ in range(n+1)]
#         # d[0][0] d[i][0]=0 前i个元素构成0需要的硬币数为0
#         # d[0][i] 为前0个元素构成i应该是-1，这里我们设置成float('inf')，最后特判一下就好
#         for i in range(n+1):
#             d[i][0] = 0
#         for i in range(1, n+1):
#             for j in range(1, amount+1):
#                 d[i][j] = min(d[i][j], d[i-1][j])
#                 if j>=coins[i-1]:
#                     d[i][j] = min(d[i][j], d[i][j-coins[i-1]]+1)
#         # print(d)
#         return d[n][amount] if d[n][amount]!=float('inf') else -1


# # # 空间优化的完全背包
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not coins: return 0
#         d = [float('inf')]*(amount+1) # d[i]价值i的是时候，最少的硬币数量
#         d[0] = 0 #需要的硬币数字
#         for val in coins:
#             for j in range(1, amount+1):
#                 if j >= val:
#                     d[j] = min(d[j], d[j-val]+1)
#         return d[-1] if d[-1] != float('inf') else -1

# # # BFS需要掌握 760ms
# class Solution: # [1] 0;当amount为0时，则返回0，所以最开始的时候step不能返回step+1
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not coins: return 0
#         q = collections.deque([amount])
#         step = 0
#         visited = set()
#         while q:
#             n = len(q)
#             for _ in range(n):
#                 temp = q.popleft()
#                 if temp == 0: return step
#                 for coin in coins:
#                     if temp - coin >= 0 and (temp-coin) not in visited:
#                         q.append(temp-coin)
#                         visited.add(temp-coin)
#             step+=1
#         return -1



# DFS 2s勉强过
# https://leetcode-cn.com/problems/coin-change/solution/ji-yi-hua-hui-su-dong-tai-gui-hua-zhu-xing-jie-shi/
# class Solution:
#     def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
#         memo = {0:0}
#         # 需要 数量为n的最小面额数量
#         def helper(n):
#             if n in memo:
#                 return memo[n]
#             res = float('inf')
#             for coin in coins:
#                 if n >= coin:
#                     res = min(res, helper(n-coin)+1)#选择了当前coin就应该+1
#             memo[n] = res 
#             return res 
#         tmp = helper(amount)
#         return tmp if tmp!=float('inf') else -1

# DFS
class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        if not coins: return 0
        self.res = float('inf')
        coins.sort(key=lambda x:-x)
        self.dfs(amount, 0, coins, 0)
        return self.res if self.res != float('inf') else -1

    def dfs(self, amount, idx, coins, cnt):
        coin = coins[idx]
        if idx == len(coins)-1:
            if amount%coin == 0:
                # print(self.res, cnt+amount//coin)
                self.res = min(self.res, cnt+amount//coin)
        else:
            k = amount//coin 
            while k>=0 and cnt+k < self.res:
                # print('K:', k)
                self.dfs(amount-k*coin, idx+1, coins, cnt+k)
                k-=1
            #  amount % coin == 0:
            # self.res = min(self.res, )
```

![](.gitbook/assets/image.png)

