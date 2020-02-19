窗口函数和双指针

![1578087673704](D:\markdwonPictures\1578087673704.png)





![1578086879490](D:\markdwonPictures\1578086879490.png)

## 对撞型

### sum

![1578063221646](D:\markdwonPictures\1578063221646.png)

排序以后，a\<b\<c:只需要判断是否a\+b\>c就可以了



**016. 3Sum closet**

**018. 4Sum**

hash方法回头看下，sum方法会了O(n^3)

![1578068000625](D:\markdwonPictures\1578068000625.png)

## 前向型

### tail类

分为remove和move问题，有固定的模板

```python
tail = 初始位置
for i in range(n)
	if nums[i] 满足条件:
        nums[i], nums[tail] = nums[tail], nums[i]//move
        nums[tail] = nums[i] //remove 
        tail += 1
       
```



027 remove element 

283 move zeros 

026 [Remove Duplicates from Sorted Array](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

080 [Remove Duplicates from Sorted Array II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/)

83 remove duplicates from sorted list 

82 remove duplicates from sorted list II

### 窗口型

![1578086709930](D:\markdwonPictures\1578086709930.png)



[209. Minimum Size Subarray Sum](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)

[ 3. Longest Substring Without Repeating Characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

[76. Minimum Window Substring](https://leetcode-cn.com/problems/minimum-window-substring/)

[30. Substring with Concatenation of All Words](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)

[159. Longest Substring with At Most Two Distinct Characters](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/)

```python

```

![1578150373204](D:\markdwonPictures\1578150373204.png)



[340. 至多包含 K 个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/)

[727. 最小窗口子序列](https://leetcode-cn.com/problems/minimum-window-subsequence/)

[632. 最小区间](https://leetcode-cn.com/problems/smallest-range/)

[567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)

[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)



