# BFS/DFS



### [139. 单词拆分](https://leetcode-cn.com/problems/word-break/)

Difficulty: **中等**

给定一个**非空**字符串 _s_ 和一个包含**非空**单词列表的字典 _wordDict_，判定 _s_ 是否可以被空格拆分为一个或多个在字典中出现的单词。

**说明：**

* 拆分时可以重复使用字典中的单词。
* 你可以假设字典中没有重复的单词。

**示例 1：**

```text
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
```

**示例 2：**

```text
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
```

**示例 3：**

```text
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```

**Solution**

Language: **Python3**

```python
​# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         # d[i]表示前i个字符（在s里面就是0~(i-1))组成的子串是否能分解成列表中的若干字符串
#         # T:O(n^2), S:O(n+m)
#         n = len(s)
#         d = [0]*(n+1)
#         d[0] = True

#         for i in range(1, n+1):
#             for j in range(i-1, -1, -1):
#                 if d[j] and s[j:i] in wordDict:
#                     # 这里是appled的时候， j=0,d[0] = True;
#                     d[i] = True
#                     break
#         print(d)
#         return d[n]

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         d = [0]*(n+1)
#         d[0] = True # d[i]表示[0,i-1]符合要求，在s里面[0,-1]为空符合 d[1] 为s[0:0]需要测试了
#         dic = {word:0 for word in wordDict}
#         for i in range(1, n+1):
#             for j in  range(i-1, -1, -1):
#                 # d[j]表示前j个字符已经拆分成功
#                 if d[j] and s[j:i] in dic:
#                     d[i] = True
#                     break
#         return d[n]

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         d = [0]*(n+1)
#         d[0] = True # d[i]表示[0,i-1]符合要求，在s里面[0,-1]为空符合 d[1] 为s[0:0]需要测试了
#         dic = {word:0 for word in wordDict}
#         for i in range(1, n+1):
#             for j in range(i-1,-1,-1):
#                 if d[j] and s[j:i] in dic:
#                     d[i] = True 
#         return d[n]
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

#         def back_track(s):
#             if(not s):
#                 return True
#             res=False
#             for i in range(1,len(s)+1):
#                 if(s[:i] in wordDict):
#                     res=back_track(s[i:]) or res
#             return res
#         return back_track(s)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        self.memo = {}
        for word in wordDict:
            dic[word] = True 
        return self.dfs(s, dic)
    def dfs(self, s, dic) -> bool:
        if s in self.memo:
            return self.memo[s]

        if s in dic:
            return True 
        for i in range(1,len(s)):
            if s[:i] in dic and self.dfs(s[i:], dic):
                self.memo[s] = True 
                return True 
        self.memo[s] = False 
        return False
```

![DFS&#x601D;&#x8003;&#x8FC7;&#x7A0B;](.gitbook/assets/image%20%281%29.png)

### [286. 墙与门](https://leetcode-cn.com/problems/walls-and-gates/)

Difficulty: **中等**

你被给定一个 _m × n_ 的二维网格，网格中有以下三种可能的初始化值：

1. `-1` 表示墙或是障碍物
2. `0` 表示一扇门
3. `INF` 无限表示一个空的房间。然后，我们用 `2<sup>31</sup> - 1 = 2147483647` 代表 `INF`。你可以认为通往门的距离总是小于 `2147483647` 的。

你要给每个空房间位上填上该房间到 _最近_ 门的距离，如果无法到达门，则填 `INF` 即可。

**示例：**

给定二维网格：

```text
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
```

运行完你的函数后，该网格应该变成：

```text
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
```

**Solution**

Language: **Python3**

```python
​class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        MAX = 2147483647
        if not rooms or not rooms[0]: return 
        n, m = len(rooms), len(rooms[0])
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        dirs = [[0, 1], [1,0], [-1,0], [0,-1]]
        while q:
            x, y, step = q.popleft()
            for d in dirs:
                newx = x+d[0]
                newy = y+d[1]
                if 0<=newx<n and 0<=newy<m and rooms[newx][newy] == MAX:
                    rooms[newx][newy] = step+1
                    q.append((newx, newy, step+1))
```

### 

#### [695. Max Area of Island](https://leetcode-cn.com/problems/max-area-of-island/)

Difficulty: **中等**

Given a non-empty 2D array `grid` of 0's and 1's, an **island** is a group of `1`'s \(representing land\) connected 4-directionally \(horizontal or vertical.\) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. \(If there is no island, the maximum area is 0.\)

**Example 1:**

```text
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
```

Given the above grid, return `6`. Note the answer is not 11, because the island must be connected 4-directionally.

**Example 2:**

```text
[[0,0,0,0,0,0,0,0]]
```

Given the above grid, return `0`.

**Note:** The length of each dimension in the given `grid` does not exceed 50.

**Solution**

Language: **Python3**

```python
​# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         res = 0
#         if not grid or not grid[0]: return res 
#         n, m = len(grid), len(grid[0])
#         visited = [[False]*m for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 res = max(res, self.dfs(grid, i, j, visited))
#         return res 
    
#     def dfs(self, grid, x, y, visited):
#         if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or visited[x][y] or grid[x][y] == 0:
#             return 0
#         visited[x][y] = True 
#         return 1 + self.dfs(grid, x+1, y, visited) \
#                  + self.dfs(grid, x, y+1, visited) \
#                  + self.dfs(grid, x, y-1, visited) \
#                  + self.dfs(grid, x-1, y, visited) \

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid or not grid[0]: return res 
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        q = collections.deque([(0, 0)])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    q = collections.deque([(i, j)])
                    temp = 1
                    visited[i][j] = visited
                    while q:
                        x_, y_ = q.popleft()
                        for d in dirs:
                            x = x_ + d[0]
                            y = y_ + d[1]   
                            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or visited[x][y] or grid[x][y] == 0:
                                continue 
                            else:
                                temp += 1
                                visited[x][y] = True 
                                q.append((x, y))
                    res = max(res, temp)
        return res
```

### [994. 腐烂的橘子](https://leetcode-cn.com/problems/rotting-oranges/)

Difficulty: **简单**

在给定的网格中，每个单元格可以有以下三个值之一：

* 值 `0` 代表空单元格；
* 值 `1` 代表新鲜橘子；
* 值 `2` 代表腐烂的橘子。

每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/oranges.png)

```text
输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
```

**示例 2：**

```text
输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
```

**示例 3：**

```text
输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
```

**提示：**

1. `1 <= grid.length <= 10`
2. `1 <= grid[0].length <= 10`
3. `grid[i][j]` 仅为 `0`、`1` 或 `2`

**Solution**

Language: **Python3**

```python
​class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return grid 
        from collections import deque 
        time = 0
        n, m = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        res = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    res.append((i, j))
        while res:
            length = len(res)
            for _ in range(length):
                x, y = res.popleft()
                for d in dirs:
                    x_new, y_new = x+d[0], y+d[1]
                    if 0<=x_new<n  and 0<=y_new<m and grid[x_new][y_new] == 1:
                        grid[x_new][y_new] = 2
                        res.append((x_new, y_new))
            time+=1
        for row in grid:
            if 1 in row:
                return -1 
        return 0 if time == 0 else time-1 # 这里最后一步多加了一步，需要-1
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return -1 
        from collections import deque 
        minute = 0
        n, m = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        stk = [(i,j) for i in range(n) for j in range(m) if grid[i][j] == 2]
        while True:
            stk_next = [] #这里加入了下一层的变量，如果变量为空，直接break，相对于上面写法，就不会后面特判-1
            while stk:
                x, y = stk.pop()
                for d in dirs:
                    n_x, n_y = x+d[0], y+d[1]
                    if 0<=n_x<n and 0<=n_y<m and grid[n_x][n_y] == 1:
                        grid[n_x][n_y] = 2 
                        stk_next.append((n_x, n_y))
            if not stk_next: break 
            stk = stk_next[:]
            minute += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return minute
```

