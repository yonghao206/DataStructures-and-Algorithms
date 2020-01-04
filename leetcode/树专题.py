# 树专题
101
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    	if not root:
    		return True

    	return self.dfs(root.left, root.right)

    def dfs(self, l, r):
    	if not l and not r:
    		return
    	if not l or not r:
    		return False
    	if l.val != r.val:
    		return False

    	l = self.dfs(l.left, r.right)
    	r = self.dfs(l.right, r.left)
    	return l and r 

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    	if not root:
    		return True
    	stack = [(root.left, root.right)]
    	while stack:
    		l, r = stack.pop()
    		if not l and not r:
    			continue 
    		if not l or not r:
    			return False
    		if l.val != r.val:
    			return False
    		stack.append((l.left, r.right))
    		stack.append((l.right, r.left))

    	return True 

100
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False 
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

111
# T:O(n); S:O(n)
# 递归函数意义：当前节点的最小深度
class Solution:
    def minDepth(self, root: TreeNode) -> int:
    	if not root:
    		return 0
    	if not root.left and not root.right:
    		return 1
    	if not root.left:
    		return 1+self.minDepth(root.right)
    	if not root.right:
    		return 1+self.minDepth(root.left)
    	return 1+min(self.minDepth(root.right), self.minDepth(root.left))

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.append(root)
        depth = 1
        # 判断能不能+1，要么是叶子节点 not node.left and not node.right都为True
        # 要么就是1+min(node.left) ....等
        while queue:
            length = len(queue)
            for i in range(length):
                temp = queue.popleft()
                if not temp.left and not temp.right:
                    return depth
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            # 层次遍历，按照层来加，位置错误
            depth += 1

        return -1

104
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
    	if not root:
    		return 0
    	left = self.maxDepth(root.left)
    	right = self.maxDepth(root.right)
    	return 1+max(left, right)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            depth += 1
        return depth

94:
c 

110
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 自己写的问题是没有考虑根节点下的位置，只考虑了根节点
# T:O(nlogn) S:O(n) 
# 时间上，是每一个节点都要往下考虑，完全二叉树的时候就是O(nlogn), 空间就是O(n)当退化成链表的时候
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         # 当前节点的左右子树高度差<=1；递归判断子节点的左右子节点的高度差
#         return abs(self.getMaxHeight(root.left)-self.getMaxHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
#     def getMaxHeight(self, node):
#         if not node:
#             return 0
#         return 1 + max(self.getMaxHeight(node.left), self.getMaxHeight(node.right))

# S:O(N) T:O(n) #这里加入了一层对子节点的判断，不用上来就是直接递归的从上往下看。
# 这里是自底向上判断

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.getHeightAndCheck(root) != -1
        
    def getHeightAndCheck(self, root):
        if not root:
            return 0
        left = self.getHeightAndCheck(root.left)
        if left == -1: 
            return -1
        right = self.getHeightAndCheck(root.right)
        if right == -1: 
            return -1
        if abs(left-right)>1:
            return -1
        return max(left, right)+1

    def getHeightAndCheck(self, root):
    	if not root: return 0
    	left = self.getHeightAndCheck(root.left)
    	if left == -1: return -1
    	right = self.getHeightAndCheck(root.right)
    	if right == -1: return -1
    	if abs(left-right)>1: return -1
    	return max(left, right)+1

098
class Solution(object):
    def isValidBST(self, root):
    	if not root:
    		return True
    	self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node, lower, upper):
    	if not node:
    		return True
    	if node.val >= upper or node.val <= lower:
    		return False 
    	return self.dfs(node.left, lower, node.val) and self.dfs(node.right, node.val, upper)


226
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
    	if not root:
    		return root
    	root.left, root.right = root.right, root.left 
    	self.

    def dfs(self, left, right):
    	if not left and not right:
    		return 
		left.val, right.val = right.val, left.val
    	self.dfs(left.left, right.right)
    	self.dfs(left.right, right.left)


112
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    	if not root:
    		return False
    	if sum == root.val:
    		return True 
    	return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    	stack = [root]
    	val = [sum]
    	while stack:
    		temp = stack.pop()
    		temp_val = val.pop()
    		if  temp_val == temp.val and not temp.left and not temp.right:
    			return True 
    		if temp.right:
    			stack.append(temp.right)
    			val.append(sum-temp.val)
    		if temp.left:
    			stack.append(temp.left)
    			val.append(sum-temp.val)
    	return False 

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False 
        stack = [(root, sum)]
        while stack:
            node, val = stack.pop()
            if  val == node.val and not node.left and not node.right:
                return True 
            if node.right:
                stack.append((node.right, sum - val))
            if node.left:
                stack.append((node.left, sum - val))
        return False

105
class Solution:
    # 返回当前preorder下的root构成的
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    	if not preorder or not inorder:
    		return None

    	node = TreeNode(preorder[0])
    	idx = inorder.index(node.val)
    	preorder.pop(0)
    	node.left = self.buildTree(preorder, inorder[:idx])
    	node.right = self.buildTree(preorder, inorder[idx+1:])
    	return node 


543:
class Solution:
	def __init__(self):
		self.res = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
    	self.maxDepth(root)
    	return self.res 


   	def maxDpeth(self, root):
   		if not root:
   			return 0
   		left = self.maxDpeth(root.left)
   		right = self.maxDpeth(root.right)
   		self.res = max(self.res, left + right)
    	return 1+max(left, right)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
    	if not root:
    		return 0
    	res = 0 
    	stack = [root]
    	depthMap = dict()
    	while stack:
    		node = stack[-1]
    		if not node.left and not depthMap.get(node.left, 0):
    			stack.append(node.left)
    		elif not node.right and not depthMap.get(node.right, 0):
    			stack.append(node.right)
    		else: # 要么左右节点为空，要么有了map值
    			stack.pop()
    			left = depthMap.get(node.left, 0)
    			right = depthMap.get(node.right, 0)
    			res = max(res, left+right)
    			depthMap[node] = left+right

    	return res


