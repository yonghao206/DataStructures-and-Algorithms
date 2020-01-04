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

s = "111221"
pointer = 0
cnt = 1
for i in range(len(s)-1):
	if s[i] == s[i+1]:
		cnt += 1
