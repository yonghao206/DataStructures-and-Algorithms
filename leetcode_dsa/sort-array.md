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

