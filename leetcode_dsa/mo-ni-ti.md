# 模拟题



### [999. Available Captures for Rook](https://leetcode-cn.com/problems/available-captures-for-rook/)

```text
​class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = 8
        # R: (i,j) , B:break: , p:+1, '.': continue 
        res = 0
        dirs = [[0,1],[0,-1], [1,0],[-1,0]]
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    for d in dirs:
                        x, y = i, j
                        while True:
                            newx, newy = x+d[0], y+d[1]
                            if newx<0 or newx>=8 or newy<0 or newy>=8:break 
                            if board[newx][newy] == '.':
                                x, y = newx, newy 
                                continue 
                            elif board[newx][newy] == 'B':break
                            else: 
                                res+=1
                                break 
                    return res 
        return res
```

