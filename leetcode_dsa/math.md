# Math



### [7. Reverse Integer](https://leetcode-cn.com/problems/reverse-integer/)

Difficulty: **简单**

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

```text
Input: 123
Output: 321
```

**Example 2:**

```text
Input: -123
Output: -321
```

**Example 3:**

```text
Input: 120
Output: 21
```

**Note:**  
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: \[−231, 231− 1\]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

**Solution**

Language: **Java**

```java
​class Solution {
    public int reverse(int x) {
        long res = 0;
        while (x!=0){
            res = res*10 + x%10;
            if(res>Integer.MAX_VALUE || res<Integer.MIN_VALUE){
                return 0;
            }
            x /= 10;
        }
        return (int)res;
    }
}
```



### 约瑟夫环 [面试题62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/) 

Difficulty: **简单**

0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

**示例 1：**

```text
输入: n = 5, m = 3
输出: 3
```

**示例 2：**

```text
输入: n = 10, m = 17
输出: 2
```

**限制：**

* `1 <= n <= 10^5`
* `1 <= m <= 10^6`

**Solution**

Language: **Python3**

```text
​class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n+1):
            res = (res+m)%i 
        return res
```

### GCP



#### [365. 水壶问题](https://leetcode-cn.com/problems/water-and-jug-problem/)

Difficulty: **该题有新题解时你将收到通知**

该题有新题解时你将收到通知

**Solution**

Language: **Python3**

```python
​class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        #原理是ax+by=z 求二元一次方程的整数解 有整数解的前提是 x与y的最大公约数 能被z整除
        # if z == 0: return False 
        # if x+y<z: return False 
        # while y != 0:
        #     x, y = y, x%y 
        # return z%x == 0
        return x + y >= z and ( (z == 0 or z == y or z == x ) or z % math.gcd(x,y) == 0 ) 
```

