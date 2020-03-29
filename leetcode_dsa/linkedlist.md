# LinkedList



### [2. Add Two Numbers](https://leetcode-cn.com/problems/add-two-numbers/)

Difficulty: **中等**

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

```text
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

**Solution**

Language: **Java**

```java
​/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode pre = dummy;
        int carry = 0;
        int val = 0;
        while (l1!=null || l2!=null || carry!=0){
            val = carry;
            if(l1!=null){
                val += l1.val;
                l1 = l1.next;
            }
            if(l2!=null){
                val += l2.val;
                l2 = l2.next;
            }
            carry = val/10;
            pre.next = new ListNode(val%10);
            pre = pre.next;
        }
        return dummy.next;
    }
}
```

### [148. Sort List](https://leetcode-cn.com/problems/sort-list/)

Difficulty: **中等**

Sort a linked list in _O_\(_n_ log _n_\) time using constant space complexity.

**Example 1:**

```text
Input: 4->2->1->3
Output: 1->2->3->4
```

**Example 2:**

```text
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

**Solution**

Language: **Python3**

```python
​# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         # T:O(nlgn) S:O(1) 自底向上的归并排序，不需要额外空间了用 bottom-to-up 
#         # 链表里操作最难掌握的应该就是各种断链啊，然后再挂接 merge(l1, l2), cut(l, n) 将链表 l 切掉前 n 个节点，并返回后半部分的链表头 #希望同学们能把双路归并和 cut 断链的代码烂记于心，以后看到类似的题目能够刷到手软
#         if not head or not head.next:
#             return head 
#         if not head.next.next and head.next.val < head.val:
#             head.val, head.next.val = head.next.val, head.val 
#             return head 
#         midpref = getMiddle(head)
#         middle, midpre.next = midpre.next, None 
#         return mergeTwoSortedLists(mergeSort(middle), mergeSort(head))
                
# class Solution:  
#     def sortList(self, head: ListNode) -> ListNode:
#         # getMiddle 方法目的
#         # 1,2,3返回2   1,2,3,4返回2, 然后先save 2.next，再让2.next = None. 
#         # 为的是彻底分开两个list
#         def getMiddle(h:ListNode):
#             if h.next:
#                 slow,fast = h,h.next
#                 while fast.next:
#                     slow = slow.next
#                     fast = fast.next.next
#                     if not fast:
#                         return slow
#                 return slow
#             else:
#                 return h
#         def mergeTwoSortedLists(l1, l2):
#             dummy = pre = ListNode(0)
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     pre.next = l1
#                     l1 = l1.next
#                 else:
#                     pre.next = l2
#                     l2 = l2.next
#                 pre = pre.next
#             pre.next = l1 or l2
#             return dummy.next
#         def mergeSort(node):
#             if not node:
#                 return None
#             if not node.next:
#                 return node
#             if not node.next.next:
#                 if node.val>node.next.val:
#                     node.val, node.next.val = node.next.val, node.val
#                 return node
#             else:
#                 midpre = getMiddle(node)
#                 middle, midpre.next = midpre.next, None
#                 return mergeTwoSortedLists(mergeSort(middle),mergeSort(node))
#         return mergeSort(head)

# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head 
#         # divide and merge
#         slow, fast = head, head.next 
#         while fast and fast.next:
#             slow = slow.next 
#             fast = fast.next.next
#         nxt = slow.next 
#         slow.next = None 
#         return self.merge(self.sortList(head), self.sortList(nxt))

#     def merge(self, l1, l2):
#         dummy = ListNode(-1)
#         cur = dummy 
#         while l1 and l2:
#             if l1.val > l2.val:
#                 cur.next = l2 
#                 l2 = l2.next 
#             else:
#                 cur.next = l1 
#                 l1 = l1.next 
#             cur = cur.next 
#         if l1: cur.next = l1 
#         if l2: cur.next = l2 
#         return dummy.next 
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head 
#         fast, slow = head.next, head 
#         first = head 
#         while fast and fast.next:
#             fast = fast.next.next 
#             slow = slow.next 
#         sec = slow.next 
#         slow.next = None 
#         return self.merge(self.sortList(first), self.sortList(sec))

#     def merge(self, l1, l2):
#         cur = ListNode(-1)
#         prev = cur 
#         while l1 and l2:
#             if l1.val > l2.val:
#                 cur.next = l2 
#                 l2 = l2.next 
#             else:
#                 cur.next = l1 
#                 l1 = l1.next 
#             cur = cur.next 
#         if l1:
#             cur.next = l1 
#         if l2:
#             cur.next = l2 
#         return prev.next 
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head 
        left, right, mid = ListNode(-1), ListNode(-1), ListNode(-1)
        ltail, rtail, mtail = left, right, mid 
        cur = head 
        val = head.val 
        while cur:
            if cur.val == val:
                mtail.next = cur 
                mtail = mtail.next 
            elif cur.val > val:
                rtail.next = cur 
                rtail = rtail.next 
            else:
                ltail.next = cur 
                ltail = ltail.next 
            cur = cur.next 
        ltail.next = None 
        mtail.next = None 
        rtail.next = None 
        left.next = self.sortList(left.next)
        right.next = self.sortList(right.next)
        self.getTail(left).next = mid.next 
        self.getTail(left).next = right.next 
        return left.next 
    
    def getTail(self, head):
        if not head or not head.next: return head 
        while head.next:
            head = head.next 
        return head
```



