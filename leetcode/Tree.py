# 容易
# 100 
# 101 
# 104 
# 107 
# 108 Convert Sorted Array to Binary Search Tree
# 110  
# 111 
# 112
# 226
# 235
# 538 
# 543 111
# 572 
# 617 
# 700
# 中等题
# 094 
# 098 
# 102 
# 105 
# 106 
# 113 
# 114 
# 144 
# 236 
# 450

# qita
# 096
# 103
# 116
# 124
# 145
# 173
# 257
# 297
# 437
# 1307


100
class Solution:
    # 判断当前node是否相等
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: # not None 为True；此句判断都为None，为True
            return True 
        if not p or not q: # 一个为None一个有值，False
            return False
        if p.val != q.val: #均不为空，值不相等，返回False
            return False 
        # 递归左右节点
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


101
class Solution: #非递归写法 BFS
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True 
        s = [(root.left, root.right)]
        while s:
            l, r = s.pop()
            if not l and not r: continue
            if not l or not r: return False 
            if l.val != r.val: return False
            s.append((l.left, r.right))
            s.append((l.right, r.left))
        return True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True 
        return self.issym(root.left, root.right)

    def issym(self, l, r):
        if not l and not r:
            return True 
        elif not l or not r:
            return False
        return l.val == r.val and self.issym(l.left, r.right) and self.issym(l.right, r.left)


104
# class Solution: #DFS
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root: return 0
#         return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution: #BFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        queue = collections.deque([root])
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            depth += 1
        return depth

107


108
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 递归中止，当为None返回
        if not nums: return 
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        # 返回node，此node为数组中点
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


110
# 这个方法不会提前终止，也是DFS
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        self.res = True

        def helper(node):
            if not node: return 0
            left = helper(node.left)
            right = helper(node.right)
            if abs(left-right)>1:
                self.res = False
            return max(left, right)+1

        helper(root)
        return self.res 
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.h(root) != -1
    # 当不满足的时候，会返回-1，提前终止操作
    # 返回当前节点节点的高度，如果大于2，直接返回-1, DFS到底，然后往回返回，途中有-1，直接返回
    def h(self, node):
        if not node: return 0
        l = self.h(node.left)
        if l == -1: return -1
        r = self.h(node.right)
        if r == -1: return -1
        return max(l, r) + 1 if abs(l-r) <2 else -1

112
# DFS, DFS+stack, 
class Solution:
    def hasPathSum(self, root, s: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return s == root.val
        return self.hasPathSum(root.left, s-root.val) or self.hasPathSum(root.right, s-root.val)
# BFS+stack
class Solution:
    def hasPathSum(self, root, ss: int) -> bool:
        if not root: return False 
        stack = [(root, ss)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right and node.val == val:
                return True 
            if node.left: stack.append((node.left, val-node.val))
            if node.right: stack.append((node.right, val-node.val))
        return False

257
# [1,2,5] => str => "->".join(list)
# return ["->".join(i) for i in res]
# 开始: temp = [] => 截至 if not node.left and not node.right: res.append(temp) return
# 每一个递归函数：加入一个节点；
# res => 每一个元素从头节点到叶子节点
# class Solution: #DFS
#     def binaryTreePaths(self, root: TreeNode) -> List[str]:
#         if not root: return root 
#         # self.res = []
#         res = []
#         self.dfs(res, root, str(root.val))
#         return res 

#     def dfs(self, res, node, level):
#         if not node.left and not node.right:
#             res.append(level)
#             return 
#         if node.left: self.dfs(res, node.left, level+"->"+str(node.left.val))
#         if node.right: self.dfs(res, node.right, level+"->"+str(node.right.val))

# [(2, 1), (3, 1)]
# [(5, 1-2),]
class Solution: # BFS
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        from collections import deque 
        if not root: return root 
        res = []
        queue = deque([(root, [])])
        while queue:
            node, tmp = queue.pop()
            if not node.left and not node.right:
                res.append("->".join(tmp+[str(node.val)]))
            if node.right:                  # [] + [val] = []
                queue.appendleft((node.right, tmp+[(node.val)]))
            if node.left:
                queue.appendleft((node.left, tmp+[(node.val)]))
        return res

437
# 前缀和 = prefix sum:  pre[i] = a[0]+a[1]..+a[i]
# pref[2] = 18 ; pref[0] = 10 
# 18-8 = 10
# dic[10] = 1 ; prefixSum - target = key  in dic: 说明是一条路径 res+=1
# d[prefixSum] = 
# 回溯问题，18：2次
# two sum: a+b = target; for i in range(n): if target - val in dic: return [i, val-i]


# class Solution:
#     def pathSum(self, root: TreeNode, val: int) -> int:
#         # 以每个节点为根节点进行往下遍历
#         # 写出dfs函数，然后递归的求解每个节点
#         if not root: return 0
#         # self.res = 0
#         res = 0
#         res += self.dfs(root, val)
#         res += self.pathSum(root.left, val)
#         res += self.pathSum(root.right, val)
#         return res 

#    1
# -2  -3 
# 1 3 -2 null
# #-1
#     # 以当前节点为根节点进行遍历，查看是否有路径满足和为val
#     def dfs(self, node, val):
#         res = 0
#         # if not node.left and not node.right and node.val != val: return res 
#         if not node: return res
#         if node.val == val: 
#             res += 1
#         res += self.dfs(node.left, val-node.val)
#         res += self.dfs(node.right, val-node.val)
#         return res 
class Solution:
    def pathSum(self, root: TreeNode, val: int) -> int:
        if not root: return 0
        self.res = 0
        #key:val => prefixSum:count
        dic = {0:1} #target = 15; prefix 15; prefix -target in key: 
        self.dfs(dic, root, 0, val)
        print(dic)
        return self.res 
    # key: count 
    # 10: 0; 15:0; 18:0; 21:0; 16:0; 17:0; 7:0
    # res: 1+1+1
    def dfs(self, dic, node, cur, val):
        if not node: return
        cur += node.val 
        # prefix -target in key
        if cur - val in dic:
            # prefixSum:count
            self.res += dic[cur - val]
        dic[cur] = dic.get(cur, 0)+1
        self.dfs(dic, node.left, cur, val)
        self.dfs(dic, node.right, cur, val)
        dic[cur] -= 1 # 没有回溯，因为有可能现在这个点存储的是前面的分支和当前没有关系。



538
#   10
#  7   13
# 1 9 12 15

# 1 7 9 10 12 13 15
# 67 66 59 50 40 28 15 
# self.sum += node.val
# node.val = self.sum
# 右 根 左 =》
class Solution: T:O(N), S:O(N)
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        self.sum = 0
        self.dfs(root)
        return root 

    def dfs(self, root):
        if not root: return 
        self.dfs(root.right)
        self.sum += root.val 
        root.val = self.sum 
        self.dfs(root.left)
#   10
#  7   13
# 1 9 12 15
# 
# 正常我们是右根左，如果我们要模拟递归栈的话，我们要 左根右
# 每次pop的时候我们更新是有顺序的，这样更新是在中间更新，
# 中间更新我们加个判断，为0则更新当前节点，为1则继续加当前节点的左右val点
# stack
# queue: level = []; for i in range(len(q)): popleft() (x)
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return root 
        stack = [(root, 1)]
        sum = 0
        while stack:
            node, cmd = stack.pop()
            if node:
                if val == 0:
                    sum+=node.val
                    node.val = sum 
                elif cmd == 1:
                    stack.append((node.left, 1))
                    stack.append((node, 0))
                    stack.append((node.right,1))
        return root


543
# 当前节点的最大直径 = 左右子树的深度相加
# 当前节点的深度 = max(left, right)+1
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 求所有节点的depth，找到最高的
        self.mx = 0
        self.dfs(root)
        return self.mx 
    # 返回的是当前节点的最大高度，顺便更新diameter
    def dfs(self, node):
        if not node: return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.mx = max(self.mx, l+r)
        return max(l, r) + 1


572
# class Solution: # s>t
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         if not s and not t: return True 
#         if not s or not t: return False 
#         return self.judge(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
#     def judge(self, s, t):
#         if not s and not t:
#             return True
#         if not s or not t:
#             return False 
#         return s.val == t.val and self.judge(s.left, t.left) and self.judge(s.right, t.right)
# ",3,4,1,2,5"
# ",4,1,2"
class Solution: #T:O(n)S:O(n)
    def isSubtree(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root2 is None:
            return False
        def PreOrder(root):
            if not root:
                return ' '
            left=PreOrder(root.left)
            right=PreOrder(root.right)
            return ','+str(root.val)+','+left+','+right
        
        serial_1=PreOrder(root1)
        serial_2=PreOrder(root2)
        return serial_2 in serial_1

617
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2 
        if not t2: return t1
        root = TreeNode(t1.val+t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root

700
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:return None 
        if root.val == val:
            return root 
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
    
中等题
    
94
# 中: 左根右=》右根左 stk.append(node.right); node.val; node.left 
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, s = [], [root]
        while s:
            node = s.pop()
            if node:
                if isinstance(node, TreeNode):
                    s.append(node.right)
                    s.append(node.val)
                    s.append(node.left)
                else:
                    res.append(node)
        return res

#   10
#  7   13
# 1 9 12 15
# self.dfs(root.left) => while 
# res.append(root.val) 
# self.dfs(root.right)
[10, 7, 1, ]
[1, ]
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stk, p = [], [], root
        while stk or p: #开始stk为空，后面都是stk不为空
            while p: #只要有left 节点，全都放入stk中
                stk.append(p)
                p = p.left 
            p = stk.pop() # pop出来的第一个只为最左边，然后去right，继续一直p=p.left 
            res.append(p.val)
            p = p.right 
        return res



102
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 为空直接返回
        if root == None: return None
        # ret用来返回， q作为队列，来存储每一层将要遍历的node
        ret = []
        from collections import deque
        q = deque([root])
        while q:
            # 用level来存每一层的元素
            level = []
            # length = len(q)
            # 只处理当前层的节点，并将节点的值放到level里面，然后append到ret里
            for i in range(len(q)):
                temp = q.popleft()
                level.append(temp.val)
                # 将queue中加入当前层的左右子节点，为下一次遍历做准备
                if(temp.left): q.append(temp.left)
                if(temp.right): q.append(temp.right)
            # 每一层的level都加入到ret
            ret.append(level)
        return ret

103
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res = []
        q = collections.deque([root])
        while q:
            level = []
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        for idx, i in enumerate(res):
            if idx%2==1:
                res[idx] = res[idx][::-1]
        return res 

113
class Solution: # 类似回溯方法 T:O(n) S:O(h)
    def pathSum(self, root: TreeNode, v: int) -> List[List[int]]:
        if not root: return None
        self.res = []
        self.dfs(root, v, [])
        return self.res 
    def dfs(self, node, val, level):
        if not node.left and not node.right and node.val == val:# 满足结果且为叶子节点
            self.res.append(level+[node.val])
        if node.left:
            self.dfs(node.left, val-node.val, level+[node.val])
        if node.right:
            self.dfs(node.right, val-node.val, level+[node.val])

class Solution: # T:O(n), S:O(h)?
    def pathSum(self, root: TreeNode, v: int) -> List[List[int]]:
        if not root: return None 
        s = [(root, [root.val])] # 把走的路径存下来而已
        res = []
        while s:
            node, level = s.pop()
            if not node.left and not node.right and sum(level) == v:
                res.append(level)
            if node.left:
                s.append([node.left, level+[node.left.val]])
            if node.right:
                s.append([node.right, level+[node.right.val]])
        return res

144
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return 
        res = []
        s = [root]
        while s:
            node = s.pop()
            if node:
                if isinstance(node, TreeNode):
                    s.extend([node.right, node.left, node.val])
                else:
                    res.append(node)
        return res
s = [root] while s: node; if node; right, left, val; else;
先加入元素每个节点直接加val，然后直接left到底，最后每一个pop出来的直接right
root->left->right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, s = [], []
        while s or root:
            while root:
                s.append(root)
                res.append(root.val)
                root = root.left 
            root = s.pop().right 
        return res


98
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.flag = True 
        self.last = float('-inf')
        self.inorder(root)
        return self.flag
    def inorder(self, node):
        if not node: return 
        self.inorder(node.left)
        if node.val <= self.last: #inorder下，从第一个数字开始遍历，且记作标记值，必须大于它node.val>self.last;不能相等
            self.flag = False 
        self.last = node.val 
        self.inorder(node.right)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.bst(root, float('-inf'), float('inf'))
    # 确定node在(lower, upper)的范围
    def bst(self, node, lower, upper):
        if not node: return True
        if node.val >= upper or node.val <= lower:#这里是or不是and，注意之间的关系
            return False
        l = self.bst(node.left, lower, node.val)
        r = self.bst(node.right, node.val, upper)
        return l and r 
class Solution(object): #当前节点大于左子树的最大值，小于右子树的最小值
    def isValidBST(self, root):
        if not root:
            return  True
        # 判断当前节点的左子树是否有效
        leftValid = (root.left == None) or root.val > self.maxval(root.left)
        rightValid = (root.right == None) or root.val < self.minval(root.right)
        return leftValid and rightValid and self.isValidBST(root.left) and self.isValidBST(root.right)
    def minval(self, node): # 返回节点而非值
            if node:
                while node.left:
                    node = node.left
                return node.val 
    def maxval(self, node):
        if node:
            while node.right:
                node = node.right
            return node.val


class Solution:
    # 返回当前preorder下的root构成的
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(inorder)
        pos = dict()
        for i in range(n):
            #把中序遍历的值存成 value:index对，后面需要用到中序的区间
            #这样存成dict，不用每次在inorder中找root都要遍历一遍，让O(n^2)=>O(n)
            pos[inorder[i]]=i
        return self.dfs(pos, preorder, inorder, 0, n-1, 0, n-1)
    
    def dfs(self, pos, preorder, inorder, pl, pr, il, ir):
        if pl > pr:
            return None
        #先取出来根节点值
        val = preorder[pl]
        root = TreeNode(val)
        # 取出来根节点在inorder的位置
        k = pos[val]
        # inorder里左子树的长度
        length = k - il # 这里k并不在左子树里面，直接k-il,不需要+1
        root.left = self.dfs(pos, preorder, inorder, pl+1, pl+length, il, il+k-1 )
        root.right = self.dfs(pos, preorder, inorder, pl+length+1, pr, k+1, ir)
        # root.left = self.dfs(pos, preorder, inorder, pl+1, pl+length, il, k-1)
        # root.right = self.dfs(pos, preorder, inorder, pl+length+1, pr, k+1, ir)
        node.left = self.dfs(pos, preorder, inorder, pl+1, pl+length, il, il-length+1)
        node.right = self.dfs(pos, preorder, inorder, pl+length+1, pr, k+1, ir)        
        return root



# T:O(n) S:O(n) 
class Solution:
    # iterative
    def preorderTraversal(self, root: TreeNode) -> List[int]:     

        stack = []
        res = [] 
        while stack or root != None:
            while root:
                res.append(root.val)
                stack.append(root)                
                root = root.left
            root = stack.pop().right
            
        return res 



class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        # BST有左边永远先扔到stack里面
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        temp = self.stack.pop()
        temp_val = temp.val
        # pop出来一个以后，增加它的右节点
        # 用while如果有左节点，全部加入到stack中
        temp = temp.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return temp_val
         

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


105
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
        # 这里的preorder时传入的一个地址，在递归地时候不断的修改它，最后为空
        # 1. 先找到前序的第一个数字为root
        # 2. 根据这个数字找到中序遍历这个数的index
        # 3. 这个index左右的长度为左右子树的长度
        # 4. pre:[20,15,7]; in:[15,20,7]
            val = preorder.pop(0)
            idx = inorder.index(val)
            node = TreeNode(val)
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])
            return node 
# class Solution:
#     # 返回当前preorder下的root构成的
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         n = len(inorder)
#         pos = dict()
#         for i in range(n):
#             #把中序遍历的值存成 value:index对，后面需要用到中序的区间
#             #这样存成dict，不用每次在inorder中找root都要遍历一遍，让O(n^2)=>O(n)
#             pos[inorder[i]]=i
#         return self.dfs(pos, preorder, inorder, 0, n-1, 0, n-1)
    
    def dfs(self, pos, preorder, inorder, pl, pr, il, ir):
        if pl > pr:
            return None
        #先取出来根节点值
        val = preorder[pl]
        root = TreeNode(val)
        # 取出来根节点在inorder的位置
        k = pos[val]
        # inorder里左子树的长度
        length = k - il # 这里k并不在左子树里面，直接k-il,不需要+1
        root.left = self.dfs(pos, preorder, inorder, pl+1, pl+length, il, il+k-1)
        root.right = self.dfs(pos, preorder, inorder, pl+length+1, pr, k+1, ir)
        # root.left = self.dfs(pos, preorder, inorder, pl+1, pl+length, il, k-1)
        # root.right = self.dfs(pos, preorder, inorder, pl+length+1, pr, k+1, ir)
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0 or len(inorder)==0 or len(preorder)!=len(inorder):
            return None
        pre_idx=0
        idx_map = {val:idx for idx,val in enumerate(inorder)} #存储index的分界点，先存起来，学习一下写法，好
        def helper(left_inorder=0 , right_inorder = len(inorder)-1):
            nonlocal pre_idx # 当前node节点val的index，每次通过+1来更新
            if left_inorder > right_inorder:
                return None
            root = TreeNode(preorder[pre_idx])
            index = idx_map[preorder[pre_idx]] # 通过pre_index找到分界点
            pre_idx+=1
            root.left = helper(left_inorder, index-1)
            root.right = helper(index+1 , right_inorder)
            return root
        return helper()

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None 
        pos = {val:idx for idx, val in enumerate(inorder)}
        n = len(preorder)
        return self.dfs(pos, preorder, inorder, 0, n-1, 0, n-1)

    def dfs(self, pos, preorder, inorder, pl, pr, il, ir):
        if pl > pr:
            return None 
        node = TreeNode(preorder[pl])
        k = pos[preorder[pl]]
        length = k - il # 左子树的长度
        node.left = self.dfs(pos, preorder, inorder, pl+1, pl+length, il, il-length+1)
        node.right = self.dfs(pos, preorder, inorder, pl+length+1, pr, k+1, ir)
        return node 

106
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         if not inorder or not postorder or len(inorder) != len(postorder):
#             return None 
#         return self.dfs(inorder, postorder)
#     def dfs(self, inorder, postorder):
#         if inorder and postorder:
#             val = postorder.pop()
#             node = TreeNode(val)
#             k = inorder.index(val)
#             node.right = self.dfs(inorder[k+1:], postorder)
#             node.left = self.dfs(inorder[:k], postorder)
#             return node 
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None 
        self.in_dict = {val:idx for idx, val in enumerate(inorder)}
        n = len(postorder)
        return self.bt(inorder, postorder, 0, n-1, 0, n-1)

    def bt(self, i, p, il, ir, pl, pr):
        if il > ir:
            return
        val = p[pr]
        k = self.in_dict[val]
        length = k - il 
        node = TreeNode(val)
        node.left = self.bt(i, p, il, il+length-1, pl, pl+length-1)
        node.right = self.bt(i, p, k+1, ir, pl+length,pr-1)
        return node 



class Solution: # 这道题不难，但是不熟悉，你需要自己先去模拟一下，然后总结经验... #DFS
    def connect(self, root: 'root') -> 'root': 
        if not root or not root.left: return root 
        root.left.next = root.right 
        if root.next:
            root.right.next = root.next.left 
        self.connect(root.left)
        self.connect(root.right)
        return root 
       

class Solution: #BFS
    def connect(self, root: 'root') -> 'root':
        if not root: return root 
        leftMost = root 
        while leftMost.left: # 确保这不是最后一层（最后一层已经通过前一层连接完毕）
            p = leftMost
            while p: # p = p.next；通过p是否为None，判断一层是否已经遍历完成
                p.left.next = p.right
                if p.next:
                    p.right.next = p.next.left 
                p = p.next 
            leftMost = leftMost.left # 遍历完成进入下一层
        return root

116
class Solution: # 这道题不难，但是不熟悉，你需要自己先去模拟一下，然后总结经验... #DFS
    def connect(self, root: 'root') -> 'root': 
        if not root or not root.left: return root 
        root.left.next = root.right 
        if root.next:
            root.right.next = root.next.left 
        self.connect(root.left)
        self.connect(root.right)
        return root 
       

class Solution: #BFS
    def connect(self, root: 'root') -> 'root':
        if not root: return root 
        leftMost = root 
        while leftMost.left: # 确保这不是最后一层（最后一层已经通过前一层连接完毕）
            p = leftMost
            while p: # p = p.next；通过p是否为None，判断一层是否已经遍历完成
                p.left.next = p.right
                if p.next:
                    p.right.next = p.next.left 
                p = p.next 
            leftMost = leftMost.left # 遍历完成进入下一层
        return root