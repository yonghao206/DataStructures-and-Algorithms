回溯问题： 树形问题
https://www.youtube.com/watch?v=78t_yHuGg-0&feature=youtu.be
https://leetcode.com/problems/subsets-ii/discuss/30156/Subset-I-II-and-Perm-I-II-Difference-Explained

017
# # DFS回溯
# class Solution: 
#     # 3^n = O(2^n) 效率比较低，家用处理n=20
#     def letterCombinations(self, digits: str) -> List[str]:
#         self.numMap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#         self.res = []  
#         if digits:
#             self.findCombination(digits, 0, "")
#         return self.res
         
#     # 函数的意义:获得digis中从index开始的所有组合的可能
#     # s：表示digits[:index-1]翻译得到的字符串
    
#     # 递归地返回    
#     # s中保存了此时从digits[0...index-1]翻译得到的一个字母字符串
#     # s寻找和digits[index]匹配的字母，获得digits[0...index]翻译得到的解
#     # findCombination:代表已经转化了[0...index-1]的字符
#     def findCombination(self, digits, idx, s):
#         if len(s) == len(digits): # idx == len(digits)
#             self.res.append(s)
#             return
#         c = digits[idx]
#         # assert int(c)<=9 and int(c)>=2
#         letters = self.numMap[int(c)]
#         for i in letters:
#             self.findCombination(digits, idx+1, s+i) 
 
# BFS 每次都穷举一层的结果放入队列中，不断的加入队列，一层处理完，把所有结果加入队列，当处理结束以后，队列中的元素为所求元素

class Solution: 
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        temp = [""]
        now = []
        if not digits:
            return []
        # 用BFS，这个时候在digits这一层，每一次循环结束都要把这个结果存下来，详单与一个大树，存下其中一层
        # 这里存下来的是temp，用now接着每一次更新一层结束的结果，然后传递给temp
        # 再让temp和新的一个digit遍历，time O(3^n)
        # 下面这个是用temp作为一个queue，写的挺好的，需要学习一波
        for i in digits:
            now = []
            for k in temp:
                for j in numMap[int(i)]:
                    now.append(k+j)
            temp = now
        
        return temp
            
            

216 combination sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k==0:
            return []
        if n<=0:
            return []
        self.n = n
        self.res = []
        self.dfs(k, n, [], 1)
        return self.res
    
    # 枚举到了第几个数字
    # 开始枚举的位置
    # 当前选择的所有数的和
    def dfs(self, k, n, unit, start):
        if k == len(unit):
            if sum(unit) == self.n:
                self.res.append(unit)
            return
        for i in range(start,11-k+len(unit)):
            unit.append(i)
            self.dfs(k, n, unit[:], i+1)
            unit.pop()


def dfs(self, nums, index, res, path):
    res.append(path)
    for i in range(index, len(nums)):
        self.dfs(nums, index+1, res, path+[nums[i]])

for i in range(2**len(nums)):
    level = []
    for j in range(len(nums)):
        if i>>j&1:
            level.append(j)

    res.append(level)


051 N-Queens
class Solution:
    def solveSudoku(self, self.board: List[List[str]]) -> None:
        """
        Do not return anything, modify self.board in-place instead.
        """
        # 八皇后和九宫格属于精确覆盖问题，已经用Dancing links完美解决，
        # rows[9][9]前9表示第几行，前[9]表示每一行代表的从1-9是否在这行存在
        # cell的shape为 9*3*3, 表示的从[0,8]的3*3的表格
        self.cols = [[False for i in range(9)] for j in range(9)]
        self.rows = [[False for i in range(9)] for j in range(9)]
        self.cell = [[[False for i in range(3)] for j in range(3)] for k in range(9)]
        self.board = board[:][:]
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != '.':
                    t = int(self.board[i][j])-1
                    # print("i, t, j", i, t, j)
                    self.rows[i][t] = self.cols[j][i] = self.cell[t][i//3][j//3] = True
        
        self.dfs(self.board, 0, 0)
        
        
    def dfs(self, self.board, x, y):
        if y == 9:
            x += 1
            y = 0
        if x == 9:
            return True
        if self.board[x][y] !='.': return self.dfs(self.board, x, y+1)
        
        for i in range(9):
            if not self.rows[x][i] and not self.cols[y][i] and not self.cell[i][x//3][y//3]:
                self.board[x][y] = str(i+1)
                self.rows[x][i] = True
                self.cols[y][i] = True
                self.cell[i][x//3][y//3] = True
                if self.dfs(self.board, x, y+1):
                    return True
                self.board[x][y] = "."
                self.rows[x][i] = False
                self.cols[y][i] = False
                self.cell[i][x//3][y//3] = False               
        return False
                    

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 八皇后和九宫格属于精确覆盖问题，已经用Dancing links完美解决，
        # rows[9][9]前9表示第几行，前[9]表示每一行代表的从1-9是否在这行存在
        # cell的shape为 9*3*3, 表示的从[0,8]的3*3的表格
        self.cols = [[False for i in range(9)] for j in range(9)]
        self.rows = [[False for i in range(9)] for j in range(9)]
        self.cell = [[[False for i in range(3)] for j in range(3)] for k in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    t = int(board[i][j])-1
                    # print("i, t, j", i, t, j)
                    self.rows[i][t] = self.cols[j][i] = self.cell[t][i//3][j//3] = True
        
        self.dfs(board, 0, 0)
        
        
    def dfs(self, board, x, y):
        if y == 9:
            x += 1
            y = 0
        if x == 9:
            return True
        if board[x][y] !='.': return self.dfs(board, x, y+1)
        
        for i in range(9):
            if not self.rows[x][i] and not self.cols[y][i] and not self.cell[i][x//3][y//3]:
                board[x][y] = str(i+1)
                self.rows[x][i] = True
                self.cols[y][i] = True
                self.cell[i][x//3][y//3] = True
                if self.dfs(board, x, y+1):
                    return True
                board[x][y] = "."
                self.rows[x][i] = False
                self.cols[y][i] = False
                self.cell[i][x//3][y//3] = False               
        return False
                    
        
            
046
# class Solution:    
#     def permute(self, nums):
#         res = []
#         if nums:
#             self.visited = [False] * len(nums)
#             self.dfs(nums, res, 0, [])
#         return res

#     def dfs(self, nums, res, index, unit):
#         if index == len(unit):
#             res.append(unit)
#             return 

#         for i in range(len(nums)):
#             if not self.visited[i]:
#                 self.visited[i] = True
#                 unit.append(nums[i])
#                 self.dfs(nums, res, index+1, unit[:])
#                 # 递归函数（上面）保证了数组回去，但是下面这些控制变量也要注意回去
#                 # visited 的变化，已经加入的元素的pop
#                 unit.pop()
#                 self.visited[i] = False
#         return 

class Solution:    
    def permute(self, nums):
        if not nums:
            return nums
        self.visited = [False] * len(nums)
        self.res = []
        self.dfs(nums, [])
        return self.res 
    # 未被访问的visited元素的所有排列数
    # 当visited全部为False时，nums=[1,2,3]则返回6种结果
    def dfs(self, nums, unit):
        if(len(unit) == len(nums)):
            self.res.append(unit)
            return 
        
        for i in range(len(nums)):
            if not self.visited[i]:
                self.visited[i] = True
                unit.append(nums[i])
                print("i: {}, unit: {}, self.visited: {}".format(i, unit, self.visited))
                self.dfs(nums, unit[:])
                unit.pop()
                self.visited[i] = False
        
        
# 使用pythonic方法(个人感觉), 因为要更改nums的递归值，所以直接改nums, 这样切片下来每次都是开辟了一个新的空间来操作（不需要担心地址问题）
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         if nums:
#             self.dfs(nums, [], res)
#         return res
    
#     def dfs(self, nums, unit, res):
#         if not nums:
#             res.append(unit)
#             return 
#         for i in range(len(nums)):
#           # 这里用切片的方法，直接剔除了nums[i]，不用再使用visited，虽然
#             self.dfs(nums[:i]+nums[i+1:], unit+[nums[i]], res)
        
        



077
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if(n<=0 or k<=0):
            return []
        res = []
        unit = []
        self.dfs(n, k, 1, unit, res)
        return res

    def dfs(self, n, k, start, unit, res):
        if len(unit) == k:
            res.append(unit)
            return 
        i = start
        # 利用剪枝提升算法效率
        # 还有k-len(unit)的空位，[i,...,n]中至少要求 k-len(unit)空位
        # 所以 n-i+1 >= k-len(unit) 这里面 i <= n+1-(k-len(unit)) 
        while i <= n+1-(k-len(unit)):
            unit.append(i)
            self.dfs(n, k, i+1, unit[:], res)
            unit.pop()
            i += 1

        return    
        
class Solution:
    def combine(self, n, k):
        self.k = k
        res = []
        self.dfs(range(1,n+1), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        #if k < 0:  #backtracking
            #return 
        if self.k == len(path):
            res.append(path)
            return # backtracking 
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
        

078
# T:O(2^N); S:O(N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        unit = []

        self.dfs(nums, unit)

    def dfs(self, nums, unit):
        self.res.append(unit)
        for idx, val in enumerate(nums):
            self.dfs(nums[:idx]+nums[idx+1:], unit+[val])

# Method01 二进制
# T:O(N*2^N) S:O(1); 一般认为nums长度不超过32
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 用二进制表示来做subset这种问题
        # 值i的二进制表示第j位是否为1 i>>j&1
        # 枚举集合的时候用二进制枚举，常用操作
        # 加减乘除比所有位运算级高
        
        # 从0到2^n-1; 看每个值的每位数是否为1，为1，则加入
        res = []
        for i in range(2**len(nums)):
            now = []
            for j in range(len(nums)): # 有几位，就要判断几次，每一位是否为1还是0
                if i>>j&1: # 每一位看是否为1，是1，则选择append对应nums的位置nums[j]
                    now.append(nums[j])
            res.append(now)
        return res
    

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums:
            n = len(res)
            for i in range(2**n):
                temp = []
                for j in range(n):
                    if i>>j&1:
                        temp.append(nums[j])
                res.append(temp)

        return res

       
079
class Solution:
    # Time: mn*3^k
    def __init__(self):
        # 让每个点都可以走四个方向的一个小技巧...写错数字坑了半天，，，专注啊
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] 
    def exist(self, board, word):
        # The word can be constructed from letters of sequentially adjacent cell
        if board:
            m = len(board)
            n = len(board[0])
            visited = [[False for i in range(n)] for j in range(m)]
            # 对每一个index为[i,j]的字母为开头进行字符串搜索，如果搜索到了，则返回true，结束
            for i in range(m):
                for j in range(n):
                    if self.searchWord(board, word, 0, visited, i, j):
                        return True
        return False
    # x,y: startx, starty: 从board[x][y]开始寻找，寻找word[index....word.size()]
    # 这个函数代表的是从[index到 size()-1] 都找到对应的word
    def searchWord(self, board, word, index, visited, x, y):
        # 当最后一个index匹配对了，往回返回
        if (index == len(word) - 1):
            return board[x][y] == word[index]
        # 对当前index进行判断，相同则继续
        if board[x][y] == word[index]:
            # 访问此点，打个标记
            visited[x][y] = True
            # 访问此点的左右上下四个点
            for val in self.directions:
                # 更新坐标
                newx = x + val[0]
                newy = y + val[1]
                # 新的坐标满足，1.在有效区域内 2.没有被访问 3.递归调用searchWord，匹配word的idx+1
                if (newx >= 0 and newx < len(board) and newy >= 0 and newy < len(board[0])):
                    if not visited[newx][newy]:
                        if self.searchWord(board, word, index+1, visited, newx, newy):
                            return True
            visited[x][y] = False
        return False
# board[newx][newy] == word[index+1]
# 判断当前index是否合法，并且判断index+1符合有效区域和没有被访问
class Solution:
    def exist(self, board, word):
        if board:
            self.direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            self.word = word
            self.m = len(board)
            self.n = len(board[0])
            self.visited = [[False for i in range(self.n)] for j in range(self.m)]
            for i in range(self.m):
                for j in range(self.n):
                    if self.searchWord(board, 0, i, j):
                        return True     
        return False
    
    # 这个函数代表的是从[index到 size()-1] 都找到对应的word
    def searchWord(self, board, index, x, y):
        if index == len(self.word) -1:
            if(board[x][y] == self.word[index]):
                return True
            
        if board[x][y] == self.word[index]:
            self.visited[x][y] = True
            for dir_ in self.direction:
                newx = x + dir_[0]
                newy = y + dir_[1]
                if newx >= 0 and newx < self.m and newy >=0 and newy < self.n:
                    if not self.visited[newx][newy]:
                        # 从index+1到结束都找到对应的word[index+1]就可以返回True
                        if self.searchWord(board, index+1, newx, newy):
                            return True
            
            self.visited[x][y] = False
        return False


200
class Solution:
    def __init__(self):
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def numIslands(self, grid: List[List[str]]) -> int:
        # The word can be constructed from letters of sequentially adjacent cell
        res = 0
        if grid:
            m = len(grid)
            n = len(grid[0])
            visited = [[False for i in range(n)] for j in range(m)]
            for i in range(m):
                for j in range(n):
                    if grid[i][j] =='1' and not visited[i][j]: #self.searchWord(grid, 1, visited, i, j):
                        res += 1
                        # 作用：标记该岛屿的所有点
                        self.dfs(grid, i, j, visited)
        return res
    # 从grid[x][y]的位置开始，进行floodfill
    # 保证(x,y)合法，且grid[x][y]是从没有被访问过的陆地
    def dfs(self, grid, x, y, visited):
        # 不是要找序列或者标记值，只是想让所有的区域都visited
        visited[x][y] = True
        for val in self.directions:
            newx = x + val[0]
            newy = y + val[1]
            # 递归终止条件被融入到了这个if语句中
            # 没有被访问过，它的其它领地是要不非法的，要不水域，要不已经访问过了
            if grid[newx][newy] == '1':
                if (newx >= 0 and newx < len(grid) and newy >= 0 and newy < len(grid[0])):
                    if not visited[newx][newy]:
                        self.dfs(grid, newx, newy, visited)
        return
        
#     def searchWord(self, board, word, visited, x, y):
#         # if (index == len(word) - 1):
#         #     if board[x][y] == word:
#         #         return True
#         #     else:
#         #         return False
#         if board[x][y] == word:
#             visited[x][y] = True
#             for val in self.directions:
#                 newx = x + val[0]
#                 newy = y + val[1]
#                 if (newx >= 0 and newx < len(board) and newy >= 0 and newy < len(board[0])):
#                     if not visited[newx][newy]:
#                         if self.searchWord(board, 1, visited, newx, newy):
#                             return True
#             visited[x][y] = False
#         return False

    
    
    
051
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False]* n
        dia1 = [False] * (2*n - 1)
        dia2 = [False] * (2*n - 1)
        # 记下每一行的index
        row = []
        self.res = []
        self.putQueen(n, 0, row, cols, dia1, dia2)
        return self.res
    # 尝试在n皇后中，拜访第index行的位置，存在row中
    def putQueen(self, n, index, row, cols, dia1, dia2):
        if index == n:
            # 这里面会递归所有的可能的结果(不会递归地是因为不符合col，dia1,dia2)
            # 只有符合这三个要求的结果n行都能拜访，才能够来到这里，来到这里以后的list是大小为n
            # 将大小为n的list转化为棋盘，然后存在res里面
            self.res.append(self.generateBoard(n, row))  
            return 
        # 尝试将第index行的皇后摆在第i列，[index, i]上，判断i是否符合col, dia1, dia2
        # 符合就继续递归到下一层index+1上，
        for i in range(n):
            # 在col，dia1，dia2没有冲突的情况下，就append 
            if not cols[i] and not dia1[index + i] and not dia2[index-i+n-1]:
                row.append(i)
                cols[i] = True
                dia1[index + i] = True
                dia2[index-i+n-1] = True
                self.putQueen(n, index + 1, row, cols, dia1, dia2)
                cols[i] = False
                dia1[index+i] = False
                dia2[index-i+n-1] = False
                row.pop()
                
    def generateBoard(self, n, row):
        board = ["."*n]*n
        for ite, idx in enumerate(row):
            temp = board[ite]
            temp = list(temp)
            temp[idx] = "Q"
            temp = "".join(temp)
            board[ite] = temp
        return board
        

022

# T:O(4^n/sqrt(n)); S:O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        unit = ''
        
        self.dfs(n, n, unit)
        return self.res
    
    def dfs(self, left, right, unit):
        if left == right == 0:
            self.res.append(unit)
        else:
            if left > 0:
                self.dfs(left-1, right, unit+'(')
            if right > left:
                self.dfs(left, right-1, unit+')')


# 排列 [1,2,3]六种方法
# 组合 [1,2,3], n, k, Cn,k
# subset: 所有组合找出来
# 39题接近subset，不同地方在于，这里可以有重复的数字，所以不用[idx+1:]改为[idx:]
# 用打印来验证自己的想法print(unit+[val])，bobo老师还是有经验啊

039
# 统计好做过的最最经典和基础的题目，从这些题目中找到相似的地方来
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        self.res = []
        self.dfs(nums, target, [])
        return self.res
    
    def dfs(self, nums, target, unit):
        if target == 0:
            self.res.append(unit)
        for idx, val in enumerate(nums):
            print(unit+[val])
            if target >= val:
                self.dfs(nums[idx:], target-val, unit+[val])

207
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0]*numCourses
        graph = dict()
        for i in rnage(len(prerequisites)):
            graph[prerequisites[i][0]] = graph.get(prerequisites[i][0], 0)+1
            