# Tree



### [543. Diameter of Binary Tree](https://leetcode-cn.com/problems/diameter-of-binary-tree/)

Difficulty: **简单**

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the **longest** path between any two nodes in a tree. This path may or may not pass through the root.

**Example:**  
Given a binary tree

```text
          1
         / \
        2   3
       / \     
      4   5
```

Return **3**, which is the length of the path \[4,2,1,3\] or \[5,2,1,3\].

**Note:** The length of path between two nodes is represented by the number of edges between them.

**Solution**

Language: **Python3**

```python
​# 当前节点的最大直径 = 左右子树的深度相加
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

    # def dfs(self, node):
    #     if not node: return 0
    #     l = self.dfs(node.left)
    #     r = self.dfs(node.right)
    #     self.mx = max(self.mx, l+r)
    #     return max(l, r)+1

```

