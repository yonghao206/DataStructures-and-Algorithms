# 题目总结(抄写代码的地方）
# https://zhuanlan.zhihu.com/p/25865715

0823 数组题目：

283
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in-place操作： Time: O(n) Space: O(1)
        # if nums:
        #     k = 0 # [0...k) 的元素均为非0
        #     # 设置两个指针，一个指0，一个非0，然后调换位置
        #     for i in range(len(nums)):
        #         if nums[i] != 0:
        #             nums[k] = nums[i]
        #             k += 1 
        #     for i in range(k, len(nums)):
        #         nums[i] = 0
        
        # 就地交换
        # 做题思路：当时想到了两个指针，但是没有确定指针的意义，第一个指针是k，[0,k)的结果是非0，[k，n)为0
        # 这样更新思路就是，当i不为0时，和num[k]进行交换，因为[0,k)为非0，然后k++ 
        if nums:
            k = 0 # [0...k) 的元素均为非0
            # 当i为0的时候，和k进行交换，然后k++，确保[0,k)为非0
            for i in range(len(nums)):
                if nums[i]:
                    if i != k:
                        nums[k], nums[i] = nums[i], nums[k]
                    k+=1
        
027 remove element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # # inplace + sorted
        # k = 0 # 设立一个k让[0,k)为你要的值
        # if nums:
        #     for i in range(len(nums)):
        #         if nums[i]!=val:
        #             if i != k:
        #                 nums[i], nums[k] = nums[k], nums[i]
        #             k+=1
        # return k
        
        l, r = 0, len(nums)-1
        if nums:
            while l <= r:
                if nums[l] == val:
                    nums[l], nums[r] = nums[r], nums[l]
                    r -= 1
                else:
                    l += 1

        return l


def threeSum(self, nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

075
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # one-pass algorithm 扫描一遍
        # # 这里所谓的三路快排
        # # 用zero i two 分别维护0，1，2的区域
        # # [:zero-1]前为0， [two+1:]为2，i为遍历指针，当nums[i] == 1是，只是i++,其他为0，2都要swap
        # zero = 0
        # i = 0
        # two = len(nums) - 1
        # while i <= two:
        #     # 为0，把这个i和zero swap一下，然后 zero,i都++
        #     if nums[i] == 0:
        #         nums[zero], nums[i] = nums[i], nums[zero]
        #         i += 1
        #         zero += 1
        #     # 为1的时候，i++
        #     # 因为我是1的时候都直接++，导致前面i走过的地方都是1，如果遇到了0，直接swap，因为前面都是1，所以交换下来的肯定是1，这样直接i++
        #     # 这也是什么在nums[i] == 2的时候，没有i++,只有two--
        #     elif nums[i] == 1:
        #         i += 1
        #     # 为2的时候 i和two swap一下，然后 two--,
        #     # 为0的时候有i++,为2的时候没有，二者只需要做一次来确定指针维护
        #     elif nums[i] == 2:
        #         nums[two], nums[i] = nums[i], nums[two]
        #         two -= 1
        # return nums
        
        zero = -1 #[0, zero]
        i = 0  # [zero+1, two-1]
        two = len(nums) #[two,len(nums)-1] 
        if nums:
            while  i < two:
                if nums[i] == 0:
                    zero += 1
                    nums[zero], nums[i] = nums[i], nums[zero]
                    i += 1
                elif nums[i] == 1:
                    i += 1
                elif nums[i] == 2:
                    two -= 1
                    nums[two], nums[i] = nums[i], nums[two]

            

查找表相关问题

219
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 用滑动窗口的思路
        # 滑动窗口，清晰的明白，你的i，i+k等元素的index，必须画图弄明白再去写代码，别急
        a = set()
        for i in range(len(nums)):
            if nums[i] in a:
                return True
            else:
                a.add(nums[i])
                if(len(a) == k+1):
                    a.remove(nums[i-k])
        return False



滑动窗口、双指针、单调队列和单调栈
https://mp.weixin.qq.com/s/6YeZUCYj5ft-OGa85sQegw

003
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = [0]*256
        l, r, res = 0, -1, 0
        while l < len(s):
            if r+1<len(s) and freq[ord(s[r+1])] == 0:
                r+=1
                freq[ord(s[r])] = 1
            else:
                freq[ord(s[l])] -= 1
                l+=1
            res = max(res, r-l+1)

        return res
method02
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, left, res = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start)
                left = dic[ch]+1
            dic[ch] = i 
        return max(res, i-start+1)

        dic, left, res = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-left)
                left = dic[ch] + 1
            dic[ch] = i



076 Minimum windown substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # a:2 需要2个a；a:-2 多了两个a，不需要的
        d = collections.Counter(t)
        cnt = len(t)
        j = 0
        res = ""
        for i in range(len(s)):
            if d[s[i]] > 0:
                cnt -= 1
            d[s[i]] -= 1
            while cnt == 0:
                if not res or len(res) < (i-j+1):
                    res = s[j:i+1]
                d[s[j]] -= 1
                if d[s[j]] > 0:
                    cnt += 1
                j += 1
        return res 

032
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 每一个左括号，对应的右括号都是确定的，不会变
        # 一个括号序列合法 等同于 所有前缀和>=0, 且总和等于0
        # )()()) : -1 1 -1 1 -1 -1 前缀和：-1，0，-1，0，-1， -2；
        # (()()()): 1,2,1,2,1,2,1,0 这个满足，前缀和大于等于0，且总和等于0
        # start当前枚举的这一段的开头； cnt前缀和[start: cur]
        # (=1; )=-1
        # 1. cnt < 0 => start=cur+1, cnt = 0
        # 2. cnt > 0 => 继续做
        # 3. cnt == 0 => [start:i]合法序列
        # 当左括号大于右括号的数量，这个时候需要需要对称的做一遍才行
        
        
        res = self.word(s)
        s = s[::-1]
        s = "".join(['(' if i == ')' else ')' for i in s])
        return max(self.word(s), res)
            
    def word(self, s):
        cnt = 0
        start = 0
        res = 0
        for i, char in enumerate(s):
            if char == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    start = i+1
                    cnt = 0
                elif cnt == 0:
                    res = max(res, i-start+1)
        return res




# 字典常见操作
# https://blog.csdn.net/xiaohuihui1994/article/details/96873918
# collecion.Counter, collection.defaultdict


链表问题：
019 remove Nth Node from end of list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        for i in range(n):
            first = first.next
        second = dummy
        while first.next != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next 

083
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            if node.val = node.next.val:
                node.next = node.next.next
            else:
                node = node.next 

        return head

061
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 1. 确定head不为空
        # 2. 找到真正的k个数
        # 3. 类似于一个题目（删除倒数第k个数）需要两个指针first 和second
        # 4. 找到指针以后，画个图，描述指针的变化即可
        if head == None: 
            return None
        count = 0
        p = head
        while(p):
            p = p.next
            count += 1
        k = k % count 
        
        #这里有个感悟： first和second指针之间的距离是k，是否有dummy不影响二者之间的距离，只要控制好平行移动就好
        # dummyNode = ListNode(-1)
        first = second = head
        for i in range(k):
            first = first.next
        while(first.next):
            first = first.next
            second = second.next
        first.next = head
        head = second.next
        second.next = None
        return head

024 Swap nodes in pairs
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            prev.next = second 
            first.next = second.next 
            second.next = first 

            # prev = 

206 Rverse Linked List
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt 

        return 

092 Reverse Linked List II
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return head 
        if m == n: return head 
        dummy = ListNode(-1)
        dummy.next = head
        a = dummy 
        for _ in range(m-1):
            a = a.next

        b = a.next 
        prev = b 
        cur = prev.next
        for _ in range(n-m):
            nxt =  cur.next
            cur.next = prev
            cur = nxt 
            prev = cur 
        a.next = prev
        b.next = cur 
        return dummy.next 

160 Intersection of two linked list
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # O(n+m) 
        p = headA
        q = headB
        while(p != q):
            if(p):
                p = p.next
            else:
                p = headB
            if(q):
                q = q.next
            else:
                q = headA
                
        return q

142 Linked List Cycle II
class Solution(object):
    def detectCycle(self, head):
        if not head: return head
        f = head 
        s = head 
        while s:
            s = s.next
            f = f.next
            if s.next:
                s = s.next 
            if f == q:
                f = head
                while f != s:
                    f = f.next
                    s = s.next
                return f

        return None


