# Sort/Array



### [8. String to Integer \(atoi\)](https://leetcode-cn.com/problems/string-to-integer-atoi/)

Difficulty: **中等**

Implement `<span style="display: inline;">atoi</span>` which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

**Note:**

* Only the space character `' '` is considered as whitespace character.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: \[−231,  231− 1\]. If the numerical value is out of the range of representable values, INT\_MAX \(231− 1\) or INT\_MIN \(−231\) is returned.

**Example 1:**

```text
Input: "42"
Output: 42
```

**Example 2:**

```text
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```

**Example 3:**

```text
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```

**Example 4:**

```text
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
```

**Example 5:**

```text
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
```

**Solution**

Language: **Python3**

```python
# 5个example的话，可以通过各种特判来避免
# 1.strip  2.sign 3.空格或者非数字停下来 4. 大于MAX小于MIN返回 MAX/MIN​
class Solution:
    def myAtoi(self, s: str) -> int: #1. 先strip然后判断是否为空，则返回0
        import sys
        res = ""
        s = s.strip()
        if not s: return 0
        i = 0
        sign = 1 # 判断sign这里，先声明变量，然后判断正负号
        if s[0] == "-":
            i += 1
            sign = -1
        elif s[0] == "+":
            i += 1
            sign = 1 
        sum = 0 
        for i in range(i, len(s)):
            if not s[i].isdigit():#如果任何一点为非数字，则直接break
                break
            sum = sum*10+int(s[i])
        sum = sum*sign  #判断是否大过 2**31-1 和 小于 -2**31 
        if sum >  2**31-1:
            return 2**31-1
        elif sum < -2**31:
            return -2**31
        else:
            return sum 
        return max(min(int(re.findall('^[\+\-]?\d+', s.lstrip())[0]), 2**31 - 1), -2**31)
```

### 

### [48. Rotate Image](https://leetcode-cn.com/problems/rotate-image/)

Difficulty: **中等**

You are given an _n_ x _n_ 2D matrix representing an image.

Rotate the image by 90 degrees \(clockwise\).

**Note:**

You have to rotate the image , which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**

```text
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**Example 2:**

```text
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

**Solution**

Language: **Python3**

```text
​class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 先转置矩阵，然后翻转每一行
        if not matrix or not matrix[0]: return matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i,n): # 沿着对角线进行翻转
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n): # 沿着中间轴进行翻转
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]: return 
        n = len(matrix)
        top, left, right, bottom = 0, 0, n-1, n-1
        i = 0
        # 外层开始一个个元素进行旋转
        while n>1:
            for i in range(n-1):
                matrix[top][left+i], matrix[top+i][right], matrix[bottom][right-i], matrix[bottom-i][left] \
         = matrix[bottom-i][left], matrix[top][left+i], matrix[top+i][right], matrix[bottom][right-i]

            top+=1
            right-=1
            bottom-=1
            left+=1
            n-=2


```

### 

### [54. Spiral Matrix](https://leetcode-cn.com/problems/spiral-matrix/)

Difficulty: **中等**

Given a matrix of _m_ x _n_ elements \(_m_ rows, _n_ columns\), return all elements of the matrix in spiral order.

**Example 1:**

```text
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**

```text
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Solution**

Language: **Python3**

```python
​class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [[0, 1], [1, 0], [0,-1], [-1,0]]
        res = []
        if not matrix or not matrix[0]: return res 
        n, m = len(matrix), len(matrix[0])
        # visited = [[False]*m for _ in range(n)]
        d = 0
        x, y = 0, 0
        for _ in range(n*m):
            res.append(matrix[x][y])
            matrix[x][y] = float('inf')
            newx, newy = x + dirs[d][0], y + dirs[d][1]
            if newx<0 or newx>=n or newy<0 or newy>=m or matrix[newx][newy]==float('inf'):
                d = (d+1)%4
                newx, newy = x + dirs[d][0], y + dirs[d][1]
            x, y = newx, newy 
        return res
```

### 

### [59. Spiral Matrix II](https://leetcode-cn.com/problems/spiral-matrix-ii/)

Difficulty: **中等**

Given a positive integer _n_, generate a square matrix filled with elements from 1 to _n_2 in spiral order.

**Example:**

```text
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

**Solution**

Language: **Python3**

```text
​class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1: return []
        res = list(range(1,n*n+1))
        x, y = 0, 0 
        visited = set()
        dirs = [[0,1], [1,0], [0,-1], [-1, 0]]
        d = 0
        ret = [[0]*n for _ in range(n)]
        for i in range(n*n):
            ret[x][y] = res[i]
            visited.add((x, y))
            newx, newy = x + dirs[d][0], y+dirs[d][1]
            if newx <0 or newx >= n or newy <0 or newy >= n or (newx, newy) in visited:
                d = (d+1)%4
                newx, newy = x + dirs[d][0], y+dirs[d][1]
            x, y = newx, newy 
        return ret 


```

### 

### [56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)

Difficulty: **中等**

Given a collection of intervals, merge all overlapping intervals.

**Example 1:**

```text
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```text
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

**Solution**

Language: **Python3**

```python
​class Solution: # O(nlogn) O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals or not intervals[0]: return res 
        intervals.sort()
        for num in intervals:
            if not res or num[0]>res[-1][1]:
                res.append(num)
            else:
                res[-1][1] = max(res[-1][1], num[1])
        return res
class Solution: # O(nlogn) O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals or not intervals[0]:return res 
        intervals.sort()
        temp = intervals[0]
        for num in intervals[1:]:
            if num[0] > temp[1]:
                res.append(temp)
                temp = num 
            else: # temp[1]>=num[0]时需要合并
                temp = [temp[0], max(temp[1], num[1])]
        res.append(temp)
        return res
```

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        // 这里list又是size来判断大小，真的恶心...
        // sort的写法，按照第一个数字来排 
        // Arrays.sort(intervals, (int[]a, int[]b)->a[0]-b[0])
        // add不需要弄个新的
        // 返回要new int[] 这个不太懂...
        if(intervals == null||intervals.length==0) return intervals;
        List<int[]> result = new ArrayList<>();
        Arrays.sort(intervals, (int[]a, int[]b)->a[0]-b[0]);
        result.add(intervals[0]);
        for(int i = 1; i<intervals.length; i++){
            int[] lastArray = result.get(result.size()-1);
            if(lastArray[1]>=intervals[i][0]){
                lastArray[1] = Math.max(lastArray[1], intervals[i][1]);
            }
            else{
                result.add(intervals[i]);
            }

        }
        return result.toArray(new int[result.size()][2]);
    
    }
}
```

## Sort

### quick, merge sort

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quick_sort(nums, 0, len(nums)-1)
        self.merge_sort(nums, [0]*len(nums), 0, len(nums)-1)
        return nums 

    def quick_sort(self, nums, l, r):
        if l >= r: return 
        i, j = l-1, r+1
        x = nums[l]
        while i < j:
            while True:
                i+=1
                if nums[i] >= x:
                    break 
            while True:
                j-=1
                if nums[j] <= x:
                    break 
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        self.quick_sort(nums, l, j)
        self.quick_sort(nums, j+1, r)
    
    def merge_sort(self, q, temp , l, r):
        if l == r: return 
        mid = l + r>> 1
        self.merge_sort(q, temp, l, mid)
        self.merge_sort(q, temp, mid+1, r)
        k, i, j = 0, l, mid+1
        while i <= mid and j <= r:
            if q[i] <= q[j]:
                temp[k] = q[i]
                i+=1
            else:
                temp[k] = q[j]
                j+=1
            k+=1
        while i <= mid:
            temp[k] = q[i]
            i+=1
            k+=1
        while j<=r:
            temp[k] = q[j]
            k+=1
            j+=1
        i, j = l, 0 
        q[l:r+1] = temp[:r-l+1]

```

### Heap

```python

```



