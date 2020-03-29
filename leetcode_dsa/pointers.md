# Pointers

![](../.gitbook/assets/image%20%283%29.png)

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

