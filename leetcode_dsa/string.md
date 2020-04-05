# String

### KMP

### [6. ZigZag Conversion](https://leetcode-cn.com/problems/zigzag-conversion/)

Difficulty: **中等**

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: \(you may want to display this pattern in a fixed font for better legibility\)

```text
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```text
string convert(string s, int numRows);
```

**Example 1:**

```text
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```text
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

**Solution**

Language: **Java**

```java
​class Solution {
    public String convert(String s, int numRows) {
        char[] c = s.toCharArray();
        int len = c.length, idx = 0;
        StringBuilder[] sb = new StringBuilder[numRows];
        for(int i = 0; i < numRows; i++){
            sb[i] = new StringBuilder();
        }
        while (idx < len){
            for(int i = 0; i < numRows && idx < len;i++){
                sb[i].append(c[idx++]);
            }
            for(int i = numRows-2; i>0 && idx < len; i--){
                sb[i].append(c[idx++]);
            }
        }
        for(int i = 1; i < numRows; i++){
            sb[0].append(sb[i]);
        }
        return sb[0].toString();
    }
}
```

```python
"""
1.第一种方法是分成n个str，一行行操作，通过更改idx和i的值
2.第二种方法， 找规律，每行每个元素相差2*(n-1)，中间行会有两个值，第二个值需要纸上确认一下是2*(n-1)-i
"""
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if not s: return ""
#         idx, i, n = 0, 0, len(s)
#         s_list = [[] for _ in range(numRows)]
#         while idx < n:
#             while idx < n and i < numRows:
#                 s_list[i].append(s[idx])
#                 idx+=1
#                 i+=1
#             i-=2
#             while idx < n and i > 0:
#                 s_list[i].append(s[idx])
#                 idx+=1
#                 i-=1
#         for i in range(1, numRows):
#             s_list[0].extend(s_list[i])
#         return "".join(map(str, s_list[0]))
class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1: return s 
        res = ""
        for i in range(n):
            if i == 0 or i == n-1:
                j = i 
                while j < len(s):
                    res += s[j]
                    j += 2*(n-1) # 每一个点的距离都是 2*(n-1)
            else:
                j = i
                k = 2*(n-1)-i #这个起始点不好想，在纸上画一下，总结规律
                while j < len(s) or k < len(s):
                    if j < len(s):
                        res+=s[j]
                        j+=2*(n-1)
                    if k < len(s):
                        res+=s[k]
                        k+=2*(n-1)
        return res
```



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
​# class Solution:
#     def myAtoi(self, s: str) -> int: #1. 先strip然后判断是否为空，则返回0
#         import sys
#         res = ""
#         s = s.strip()
#         if not s: return 0
#         i = 0
#         sign = 1 # 判断sign这里，先声明变量，然后判断正负号
#         if s[0] == "-":
#             i += 1
#             sign = -1
#         elif s[0] == "+":
#             i += 1
#             sign = 1 
#         sum = 0 
#         for i in range(i, len(s)):
#             if not s[i].isdigit():#如果任何一点为非数字，则直接break
#                 break
#             sum = sum*10+int(s[i])
#         sum = sum*sign  #判断是否大过 2**31-1 和 小于 -2**31 
#         if sum >  2**31-1:
#             return 2**31-1
#         elif sum < -2**31:
#             return -2**31
#         else:
#             return sum 
#         return max(min(int(re.findall('^[\+\-]?\d+', s.lstrip())[0]), 2**31 - 1), -2**31)
# class Solution:
#     def myAtoi(self, s: str) -> int: #1. 先strip然后判断是否为空，则返回0
#         # 1.strip  2.sign 3.空格或者非数字停下来 4. 大于MAX小于MIN返回 MAX/MIN
#         s = s.strip()
#         if not s: return 0 
#         res = 0
#         idx = 0
#         MAX = 2**31-1
#         MIN = -2**31 
#         sign = 1
#         if s[0] == "-":
#             sign = -1
#             idx = 1 
#         elif s[0] == '+':
#             idx = 1 
#             sign = 1 
#         for i in range(idx, len(s)):
#             if s[i].isdigit():
#                 res = res*10+int(s[i])
#                 if res*sign > MAX:
#                     return MAX 
#                 elif res*sign < MIN:
#                     return MIN 
#             else:
#                 return sign*res 
#         return sign * res 
class Solution:
    def myAtoi(self, s: str) -> int: 
        res = re.match('[\+\-]?\d+', s.lstrip())
        if res == None:
            return 0
        else:
            res= int(res.group())
            return max(min(res, 2**31-1), -2**31)
        # return max(min(int(*re.match('[\+\-]?\d+', s.lstrip()).group()), 2**31 - 1), -2**31)
```

