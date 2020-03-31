# Sort/Array



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

