# Pointers

![](../.gitbook/assets/image%20%2817%29.png)

### [1. Two Sum](https://leetcode-cn.com/problems/two-sum/)

Difficulty: **简单**

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have _**exactly**_ one solution, and you may not use the _same_ element twice.

**Example:**

```text
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

**Solution**

Language: **Java**

```java
​import java.util.HashMap;
import java.util.Map;
//S:O(n), T:O(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indexs = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if( map.containsKey(nums[i])){
                return new int[]{i, map.get(nums[i])};
            }
            else{
                map.put(target-nums[i], i);
            }
        }
        return new int[]{-1, -1};
    }
}
```



### [3. Longest Substring Without Repeating Characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

Difficulty:  **Example 1: Input: "abcabcbb" Output: 3 Explanation: The answer is "abc", with the length of 3. Example 2: Input: "bbbbb" Output: 1 Explanation: The answer is "b", with the length of 1. Example 3: Input: "pwwkew" Output: 3 Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.** 

Given a string, find the length of the **longest substring** without repeating characters.

**Example 1:**

```text
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3\.
```

**Example 2:**

```text
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```text
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3\. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Solution**

Language: **Java**

```java
​class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        HashMap<Character, Integer> map = new HashMap<>();
        int res = 0, start =0;
        for(int i =0; i<n; i++){
            char temp = s.charAt(i);
            if(map.containsKey(temp)){
                start = Math.max(start, map.get(temp)+1);
            }
            map.put(s.charAt(i), i);
            res = Math.max(i-start+1, res);
        }
        return res;
    }
}
```



### [42. Trapping Rain Water](https://leetcode-cn.com/problems/trapping-rain-water/)

Difficulty: **困难**

Given _n_ non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)  
The above elevation map is represented by array \[0,1,0,2,1,0,1,3,2,1,2,1\]. In this case, 6 units of rain water \(blue section\) are being trapped. **Thanks Marcos** for contributing this image!

**Example:**

```text
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Solution**

Language: **Python3**

```python
​class Solution: #O(n)
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        peak_index = 0
        water = 0
        for i in range(n):
            if height[i] > height[peak_index]:
                peak_index = i
        leftMost = 0 # 从左边开始数，扫描到的最高的点，它决定了左边的挡板高度，如果遇到后面的index没有他高，返回插值即为当前水位，如果比它高，则替换leftMost
        # 用leftmost和i来记录单调递减的地方；用peak_index把两边分开
        for i in range(peak_index):
            if height[i] > height[leftMost]:
                leftMost = i 
            elif height[i] < height[leftMost]:
                water += height[leftMost] - height[i]
        rightMost = n -1 # 从右边开始数，扫描到的最高的点，它决定了右边的挡板高度，如果遇到前面的index没有他高，返回插值即为当前水位，如果比它高，则替换rightMost
        for i in range(n-1,peak_index,-1):
            if height[i] > height[rightMost]:
                rightMost = i 
            elif height[i] < height[rightMost]:
                water += height[rightMost] - height[i]
        return water
        
# 维护一个递减的单调栈，如果遇到大于栈顶的值，pop出来，然后算一下两边的高度和长度，求解水池的容量
class Solution: #O(n)
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res = 0
        idx = 0
        stk = []
        n = len(height)
        while idx < n:
            while stk and height[idx] > height[stk[-1]]:
                top = stk.pop()
                if not stk:
                    break 
                hei = min(height[idx], height[stk[-1]]) - height[top]
                res += hei*(idx-stk[-1]-1)
            stk.append(idx)
            idx+=1
        return res 
```

### [75. Sort Colors](https://leetcode-cn.com/problems/sort-colors/)

Difficulty: **中等**

Given an array with _n_ objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

**Note:** You are not suppose to use the library's sort function for this problem.

**Example:**

```text
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Follow up:**

* A rather straight forward solution is a two-pass algorithm using counting sort.  

  First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

* Could you come up with a one-pass algorithm using only constant space?

**Solution**

Language: **Python3**

```python
​class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        one-pass algorithm 扫描一遍
        这里所谓的三路快排
        用zero i two 分别维护0，1，2的区域
        [:zero-1]前为0， [two+1:]为2，i为遍历指针，当nums[i] == 1是，只是i++,其他为0，2都要swap        """
        zero = 0
        i = 0
        two = len(nums) - 1
        while i <= two:
            # 为0，把这个i和zero swap一下，然后 zero,i都++
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
                zero += 1
            # 为1的时候，i++
            # 因为我是1的时候都直接++，导致前面i走过的地方都是1，如果遇到了0，直接swap，因为前面都是1，所以交换下来的肯定是1，这样直接i++
            # 这也是什么在nums[i] == 2的时候，没有i++,只有two--
            elif nums[i] == 1:#让[zero:i-1]为1
                i += 1
            # 为2的时候 i和two swap一下，然后 two--,
            # 为0的时候有i++,为2的时候没有，二者只需要做一次来确定指针维护
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1
        return nums

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         if not nums: return 
#         l, r , i = -1, len(nums), 0 
#         # 0:[:l], 1:[l+1, i-1]  2:[r:]
#         while i < r: #这里不用=，因为r时包含在2中的，所以不应该=
#             if nums[i] == 2:
#                 r-=1 # 给2腾出来位置，但是i的位置不变，因为你并不知道换了以后是什么数字
#                 nums[i], nums[r] = nums[r], nums[i]
#             elif nums[i] == 0:
#                 l+=1 # 给0腾位置，
#                 nums[i], nums[l] = nums[l], nums[i]
#                 i+=1 #这里nums[l]为1，所以交换了以后要++
#             else:
#                 i+=1
```

