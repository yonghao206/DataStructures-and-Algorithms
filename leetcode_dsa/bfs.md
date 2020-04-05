# BFS



#### [542. 01 Matrix](https://leetcode-cn.com/problems/01-matrix/)

Difficulty: **中等**

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

**Example 1:**

```text
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```

**Example 2:**

```text
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```

**Note:**

1. The number of elements of the given matrix will not exceed 10,000.
2. There are at least one 0 in the given matrix.
3. The cells are adjacent in only four directions: up, down, left and right.

**Solution**

Language: **Python3**

```text
​
```

![](../.gitbook/assets/image%20%284%29.png)

### [1162. As Far from Land as Possible](https://leetcode-cn.com/problems/as-far-from-land-as-possible/)

Difficulty: **中等**

Given an N x N `grid` containing only values `0` and `1`, where `0` represents water and `1` represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the _Manhattan distance_: the distance between two cells `(x0, y0)` and `(x1, y1)` is `|x0 - x1| + |y0 - y1|`.

If no land or water exists in the grid, return `-1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/05/03/1336_ex1.JPG)

```text
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/05/03/1336_ex2.JPG)

```text
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
```

**Note:**

1. `1 <= grid.length == grid[0].length <= 100`
2. `grid[i][j]` is `0` or `1`

**Solution**

Language: **Python3**

```python
​# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         if not grid or not grid[0]: return -1
#         # maxmin(W_i, L_i)
#         # BFS for each zero point
#         q = collections.deque()
#         n, m = len(grid), len(grid[0])
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 0:
#                     q.append((i,j))
#         res = -1
#         dirs = [[1,0],[-1,0],[0,1],[0,-1]]
#         if len(q) == n*m: return res 
#         while q:
#             x, y = q.popleft()
#             visited = [[False]*m for _ in range(n)]
#             visited[x][y] = True 
#             temp_q = collections.deque()
#             temp_q.append((x, y))
#             flag = False 
#             while temp_q:
#                 x_temp, y_temp = temp_q.popleft()
#                 for d in dirs:
#                     newx, newy = x_temp+d[0], y_temp+d[1]
#                     if 0<=newx<n and 0<=newy<m and not visited[newx][newy]:
#                         visited[newx][newy] = True 
#                         if grid[newx][newy] == 1:
#                             res = max(res, self.distance(newx, newy, x, y))
#                             flag = True 
#                             break 
#                         else:
#                             temp_q.append((newx, newy))
#                 if flag:break 
#         return res 

#     def distance(self, x, y, i, j):
#         return abs(x-i) + abs(y-j)
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return -1
        n, m = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
        flag = False 
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            x, y = q.popleft()
            for d in dirs:
                newx, newy = d[0]+x, d[1]+y 
                if newx<0 or newx>=n or newy<0 or newy >= m or grid[newx][newy] != 0:
                    continue 
                q.append((newx, newy))
                grid[newx][newy] = grid[x][y] + 1
                flag = True 

        if not flag: return -1 
        return grid[x][y] -1 


```

```java
class Solution {
    public int maxDistance(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        Queue<int[]> q = new ArrayDeque<>();
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        for(int i = 0; i<n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j]==1) q.offer(new int[]{i,j});
            }
        }
        boolean hasOcean = false;
        int[] p = null;
        while(!q.isEmpty()){
            p = q.poll();
            int x = p[0], y = p[1];
            for(int i = 0; i < 4; i++){
                int newx = x+dx[i];
                int newy = y+dy[i];
                if (newx<0 || newx>=n || newy<0 || newy>=m || grid[newx][newy]!=0)continue;
                grid[newx][newy] = grid[x][y] + 1;
                q.offer(new int[]{newx, newy});
                hasOcean = true;
            }
        }
        if (!hasOcean)return -1;
        return grid[p[0]][p[1]]-1;
    }
}
```

