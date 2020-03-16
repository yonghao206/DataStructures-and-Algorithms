# DP

## DP

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

