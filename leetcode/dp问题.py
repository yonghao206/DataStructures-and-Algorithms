# dp专题LC题目和yxc的DP题目：







130
# class Solution:
#     def integerBreak(self, n: int) -> int:
#     	self.max = [-1]*(n+1)
#     	return self.dfs(n)
#     # dfs(n)代表的是把n分解后的最大值
#     # dfs(2) = 1, dfs(3) = max(1*1*1, 1*2) = 2
#     # dfs(4) = max(1*1*1*1, 1*2*1, 1*3) = 3...
#   	# dfs一个函数里面只能算一个，所以如果n被分成 x份，需要调用x-1次函数
#     def dfs(self, n):
#     	if n==1:
#     		return 1
#     	if self.max[n] != -1:
#     		return self.max[n]
#     	res = -1
#     	for i in range(1, n):
#     		res = max(res, i*(n-i), i*self.dfs(n-i))
#     	self.max[n] = res
#     	return res

class Solution:
    def integerBreak(self, n: int) -> int:
    	memo = [-1] * (n+1)
    	memo[1] = 1
    	for i in range(2, n+1):


198
class Solution:
    def rob(self, nums: List[int]) -> int:
    	self.max = [-1] * len(n)
    	return self.dfs(nums, 0)

    # dfs代表的[idx:n-1]能够获取的最大值
    def dfs(self, nums, idx):
    	if idx == len(nums)-1:
    		return nums[len(nums)-1]
    	if idx == len(nums)-2:
    		return nums[len(nums)-2]
    	if self.max[idx] != -1:
    		return self.max[idx]
    	res = 0
    	for i in range(n-2):
    		res = max(res, num[i]*self.dfs(nums, idx+2))
    	self.max[idx] = res
    	return res 

120
# f[i,j]表示第i行第j列的最小值
# f[i,j] = min(f[i-1,j-1], f[i-1,j])+nums[i,j]
class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:
        n = len(nums)
        f = [[0]*n for i in range(n)]
        f[0][0] = nums[0][0]
        for i in  range(1,n):
            for j in range(i+1):
                if j == 0:
                    f[i][j] = f[i-1][j] + nums[i][j]
                elif j == i:
                    f[i][j] = min(f[i][j], f[i-1][j-1]+nums[i][j])
                else:
                    f[i][j] = min(f[i-1][j],f[i-1][j-1])+nums[i][j]
        return min(f[n-1])


063
class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        if not g: return 0
        n = len(g)
        m = len(g[0])
        f = [[0]*n for i in range(m)]
        for i in range(n):
            for j in range(m):
                if g[i][j]:
                    continue
                if i > 0:
                    f[i][j] += f[i-1][j]
                if j > 0:
                    f[i][j] += f[i][j-1]

        return f[n-1][m-1]
class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m = len(g)
        n = len(g[0])
        d = [0]*n
        d[0] = 0 if g[0][0] else 1
        for i in range(m):
            d[0] = 0 if g[i][0] else d[0]
            for j in range(1, n):
                d[j] = 0 if g[i][j] else d[j-1]+d[j]

        return d[n-1]

300
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        rse = 0
        if nums:
            n = len(nums)
            f = [1]*n
            for i in range(n):
                for j in range(i-1):
                    if nums[i] > nums[j]:
                        f[i] = max(f[i], f[j]+1)
            res = max(f)

        return res

005
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return ""
        res = ""
        n = len(s)
        d = [[0]*n for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i,n):
                d[i][j] = s[i] == s[j] and (j-i<3 or d[i+1][j-1])
                if d[i][j] and j-i+1>len(res):
                    res = s[i:j+1]
        return res 

053 Maximum Subarray 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 先考虑暴力角度：枚举所有起点和终点，然后求max([i,j])
        # DP不要枚举所有可能，用某个数来替代一类，每一类分别求，然后取 **极值**
        
        # 从集合角度来考虑DP问题
        # f[i]: 表示以i结尾的子段的最大值：max(f(i-1),0)+nums[i] 这里如果f(i-1)为负数，则不考虑前面的，只用nums[i]
        # res 返回所有的f[i]从range(n)中的最大值
        n = len(nums)
        if not nums:
            return 0
        # res = [-1] * n
        last = 0
        res = float('-inf')
        for i in range(n):
            now = max(last, 0)+nums[i]
            res = max(res, now)
            last = now
        return res

lonest common subsequence
def lcs_dp(a, b):
    a_length = len(a)
    b_length = len(b)
    value_table = [[0]*(b_length+1) for i in range(a_length+1)]
    for i in range(1, a_length+1):
        for j in range(1, b_length+1):
            if a[i-1] == b[j-1]:
                value_table[i][j] = value_table[i-1][j-1] + 1
            else:
                value_table[i][j] = max(value_table[i-1][j], value_table[i][j-1])
    return value_table, value_table[a_length][b_length]

a = "ABCDGH"
b = "AEDFHR"
table, value = lcs_dp(a, b)
table
value



DP学习
https://zhuanlan.zhihu.com/p/31628866
01背包问题：
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次
第 i 件物品的体积是 vi，价值是 wi
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大， 输出最大价值。

完全背包问题：每个物品无限多

多重背包问题：物品个数不一样

分组背包问题：物品有N组，每组若干个，每个组里面互斥一些物品






343:        
class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1]*(n+1)
        memo[1] = 1
        for i in range(1,n+1):
            for j in range(1, i):
                memo[i] = max(memo[i], j*(i-j), j*memo[i-j])

        return memo[i]



198：

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        # memo[i] 表示[0, i]的最大值
        # 求memo[n-1]  memo[n-1] = max{v[n-1]+memo[n-3], v[n-2]+memo[n-4] 。。。。 v[2]+memo[0], v[1], v[0]}
        # 这里从[n-1], [n-2]。。。 [1] 迭代的计算这些值
        # memo[i] = max(memo[i], nums[j] + memo[i+2])
        # f(0) = max(v(0)+f(2), v(2)+f(4).... v(n-2)+f(n), v(n-1))

        # f(n) = 
        memo = [-1]*n
        memo[0] = nums[-]
        for i in range(1, n):
            for j in range(i,-1,-1):
                memo[i] = max(memo[j], nums[j] + (memo[j-2] if j-2>=0 else 0))

        return memo[0]

# 0-1背包问题 dfs求解
class Knapsack01:
    # C是容量值
    # w和v都是一个数组长度为n
    def knapsack01(self, w, v, C):
        n = len(w)
        # self.memo这个矩阵是 n * (C+1)
        # n是总共n个物品，C+1是从[0, C]的结果
        # 记录的是放进去前n个文件，weight为C+1的时候对应的 value值
        # 那整个矩阵最大value就是整个矩阵右下角了
        self.memo = [[-1 for i in range(C+1)] for j in range(n)]
        return self.bestValue(w, v, n-1, C)

    # 用[0...index]的物品，去填充容积为c的背包的最大价值
    # w各个物品所对应的weight, v代表各个价值，index正在考虑的前index个物品
    def bestValue(self, w, v, index, c):
        if index < 0 or c <= 0:
            return 0
        # 可以放前index个物品时，对应的c已经被填充，则
        if self.memo[index][c] != -1:
            return self.memo[index][c]
        res = self.bestValue(w, v, index-1, c)
        if c >= w[index]:
            res = max(res, v[index] + self.bestValue(w,v, index-1, c - w[index]))

        self.memo[index][c] = res
        return res


# 0-1背包问题 dp求解
def knapsack01(self, w, v, C):
    assert(len(w) == len(v))
    n = len(w)
    if n == 0: return 0
    # capacity从[0, C]申请空间为C+1, n行的物品
    self.memo = [[-1 for i in range(C+1)] for j in range(n)]
    for j in range(C+1):
        self.memo[0][j] = (v[0] if j >= w[0] else 0)

    for i in range(1, n):
        for j in range(C+1):
            self.memo[i][j] = self.memo[i-1][j]
            if j >= w[i]:
                self.memo[i][j] = max(self.memo[i][j], v[i] + self.memo[i-1][j-w[i]])

    return self.memo[n-1][C]

# 0-1背包问题 dp求解 优化空间O(2C)
def knapsack01(self, w, v, C):
    assert(len(w) == len(v))
    n = len(w)
    if n == 0: return 0
    self.memo = [[-1 for i in range(C+1)] for j in range(2)]
    for j in range(C+1):
        self.memo[0][j] = (v[0] if j >= w[0] else 0)

    for i in range(1, n):
        # 空间只有两行，对于所有的memo设计行的都%2
        for j in range(C+1):
            self.memo[i%2][j] = self.memo[(i-1)%2][j]
            if j >= w[i]:
                self.memo[i%2][j] = max(self.memo[i%2][j], v[i] + self.memo[(i-1)%2][j-w[i]])

    return self.memo[n-1][C]

# 0-1背包问题 dp求解 优化空间O(C)
def knapsack01(self, w, v, C):
    assert(len(w) == len(v))
    n = len(w)
    if n == 0: return 0
    self.memo = [-1 for i in range(C+1)]
    for j in range(C+1):
        self.memo[j] = (v[0] if j >= w[0] else 0)

    for i in range(1, n):
        # 当memo只是一维的时候，需要从后往前遍历
        # 因为更新第i个节点的时候，我们是需要的前一行第i个元素和前面的 j-w[i]这个元素
        # 从后往前不会覆盖元素
        for j in range(C, w[i]-1, -1 ):
            self.memo[j] = max(self.memo[j], v[i] + self.memo[j-w[i]])

    return self.memo[C]





# 416 dfs
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_total = sum(nums)
        if not sum_total:
            return False
        if sum_total%2 != 0:
            return False
        # self.memo[i][c] 表示使用索引为[0...i]的这些元素，是否可以完全填充一个容量为c的背包
        # -1表示未计算；0表示不可以填充，1表示可以填充
        self.memo = [[-1 for i in range(sum_total//2+1)] for j in range(len(nums))]
        return self.dfs(nums, len(nums)-1, sum_total//2)
        
        # 使用nums[0...index]是否可以完全填充一个为sum的背包
    def dfs(self, nums, index, total):
        if total == 0:
            return True
        if total < 0 or index < 0:
            return False
        if self.memo[index][total] != -1:
            return self.memo[index][total]
        self.memo[index][total] =  self.dfs(nums, index-1, total) or self.dfs(nums, index-1, total - nums[index])
        return self.memo[index][total]

# 416 bp
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_total = sum(nums)
        if not sum_total:
            return False
        if sum_total%2 != 0:
            return False 
        n = len(nums)
        C = sum_total//2
        self.memo = [False] * (C+1)
        for i in range(C+1):
            memo[i] = nums[0] == i 
        for i in range(1,n):
            for j in range(C, nums[i]-1, -1):
                memo[j] = memo[j] or memo[j - nums[i]]
        return memo[C]



yxc 
01背包问题：

# def solve(n, t, w, v):
#     memo = [[0 for i in range(t+1)] for j in range(n+1)]
    
#     for i in range(1,n+1):
#         for j in range(0, t+1):
#             memo[i][j] = memo[i-1][j]
#             if j>=v[i]:
#                 memo[i][j] = max(memo[i][j], memo[i-1][j-v[i]]+w[i])

#     return memo


# if __name__ == '__main__':
#     # n物品数, t容量数， 
#     # 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积
#     n, t = map(int, input().strip().split())
#     v = [0 for j in range(n + 1)] # 体积
#     w = [0 for i in range(n + 1)] # 价值
#     for i in range(1, n + 1):
#         v[i], w[i] = map(int, input().strip().split())
#     # 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值
#     print("n: {}, t: {}, w: {}, v:{}".format(n, t, w, v))
#     ans = solve(n, t, w, v) #返回的是矩阵shape：[n+1, t+1]
#     print(ans[n][t])


def solve(n, t, w, v):
    memo = [0 for i in range(t+1)]
    
    for i in range(1,n+1):
        for j in range(t, v[i]-1, -1):
            memo[j] = max(memo[j], memo[j-v[i]]+w[i])
    return memo


if __name__ == '__main__':
    # n物品数, t容量数， 
    # 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积
    n, t = map(int, input().strip().split())
    v = [0 for j in range(n + 1)] # 体积
    w = [0 for i in range(n + 1)] # 价值
    for i in range(1, n + 1):
        v[i], w[i] = map(int, input().strip().split())
    # 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值
    # print("n: {}, t: {}, w: {}, v:{}".format(n, t, w, v))
    ans = solve(n, t, w, v) #返回的是矩阵shape：[n+1, t+1]
    print(ans[t])





多重背包问题：
# def solve(n, t, v, w):
#     memo = [[0]*(t+1) for i in range(n+1)]
    
#     for i in range(1, n+1):
#         for j in range(0,t+1):
#             memo[i][j] = memo[i-1][j]
#             if j>=v[i]:
#                 memo[i][j] = max(memo[i-1][j], memo[i][j-v[i]]+w[i])
#             # for k in range(j+1): 
#             #     #这里正确应该是 k=0到 k*v[i]<=j 但是我们不能够动态的改变这个(C++: for(int k=0; k*v[i]<=j; k++)
#             #     if j>=k*v[i]: # 当v[i]为1的时候，k最多是j次，所以设置为 k in range(j+1)
#             #         memo[i][j] = max(memo[i][j], memo[i-1][j-k*v[i]]+k*w[i])
#             #     else:
#             #         break
#     return memo
    
def solve(n, t, v, w):
    memo = [0]*(t+1)
    
    for i in range(1, n+1):
        for j in range(v[i], t+1):
        # for j in range(0,t+1):
            # 当优化为一维的时候，因为横坐标没有了，memo的第一部分全部删除，memo[j] = memo[j]完全相等，就直接删掉
            # memo[i][j] = memo[i-1][j]
            
            # 这里不同于01背包问题，需要j从后往前走，完全背包是在同一个i上进行更新，且j>j-v[i]，当更新j时，j-v[i]已经更新了
            # 这里不需要再让j从后往前走了
            # if j>=v[i]:
            #     memo[i][j] = max(memo[i][j], memo[i][j-v[i]]+w[i])
            memo[j] = max(memo[j], memo[j-v[i]]+w[i])

    return memo

if __name__ == "__main__":
# 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
# 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值。
    n, t = map(int, input().strip().split())
    v = [0] * (n+1)
    w = [0] * (n+1)
    for i in range(1,n+1):
        v[i], w[i] = map(int, input().strip().split())
        
    a = solve(n, t, v, w)
    print(a[t])
    
    
    


01背包和多重背包区别：
01背包的优化写法
def solve(n, t, w, v):
    memo = [0 for i in range(t+1)]
    
    for i in range(1,n+1):
        for j in range(t, v[i]-1, -1): #[t, v[i]]
            memo[j] = max(memo[j], memo[j-v[i]]+w[i])
    return memo

01背包和完全背包的二者差别只是在j的顺序上是反的，可以适当记忆，但是要理解
完全背包的优化写法：   
def solve(n, t, v, w):
    memo = [0]*(t+1)
    
    for i in range(1, n+1):
        for j in range(v[i], t+1): #[v[i], t]
        # for j in range(0,t+1):
            # 当优化为一维的时候，因为横坐标没有了，memo的第一部分全部删除，memo[j] = memo[j]完全相等，就直接删掉
            # memo[i][j] = memo[i-1][j]
            
            # 这里不同于01背包问题，需要j从后往前走，完全背包是在同一个i上进行更新，且j>j-v[i]，当更新j时，j-v[i]已经更新了
            # 这里不需要再让j从后往前走了
            # if j>=v[i]:
            #     memo[i][j] = max(memo[i][j], memo[i][j-v[i]]+w[i])
            memo[j] = max(memo[j], memo[j-v[i]]+w[i])
    return memo



贪心问题：
455
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        g_idx = 0
        s_idx = 0
        g_idx_total = len(g)
        s_idx_total = len(s)
        count = 0
        while g_idx < g_idx_total and s_idx < s_idx_total:
            if s[s_idx] >= g[g_idx]:
                count += 1
                s_idx += 1
            g_idx += 1                
        return count


264:
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [0] * n
        nums[0] = 1
        p2 = p3 = p5 = 0
        for i in range(1,n):
            nums[i] = min(nums[p2]*2, nums[p3]*3, nums[p5]*5)
            if nums[i] == nums[p2]: p2+=1
            if nums[i] == nums[p3]: p3+=1
            if nums[i] == nums[p5]: p5+=1
        return nums[-1]


139
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = [0]*(n+1)
        d[0] = True # d[i]表示[0,i-1]符合要求，在s里面[0,-1]为空符合 d[1] 为s[0:0]需要测试了
        dic = {word:0 for word in wordDict}
        for i in range(1, n+1):
            for j in  range(i-1, -1, -1):
                # d[j]表示前j个字符已经拆分成功
                if d[j] and s[j:i] in dic:
                    d[i] = True
                    break
        return d[n]