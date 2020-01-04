from collections import deque 
import numpy as np 

class BST:
    class _Node:
        def __init__(self, e):
            self.e = e
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size 

    def isEmpty(self):
        return self._size == 0

    def add(self, e):
        self._root = self._add(self._root, e)

    # return current node after new elmeent is inserted 
    def _add(self, node, e):
        # base case: if current node is None
        if not node:
            self._size += 1
            return self._Node(e)
        # if current node is not None, recursively pass the value into node's son
        if node.e == e:
            return node 
        elif node.e > e:
            node.left = self._add(node.left, e)
        else:
            node.right = self._add(node.right, e)
        return node 
    # go through the tree from root
    def contains(self, e):
        return self._contains(self._root, e)

    # check whether the tree which based on root node contains element e
    def _contains(self, node, e):
        if not node:
            return False
        if node.e == e:
            return True
        elif node.e > e:
            return self._contains(node.left, e)
        elif node.e < e:
            return self._contains(node.right, e)

    # tranverse
    def preOrder(self):
        self._preOrder(self._root)

    def _preOrder(self, node):
        if not node:
            return 
        print(node.e)
        self._preOrder(node.left)
        self._preOrder(node.right)

    def preOrderNR(self):
        stack = []
        stack.append(self._root)
        while stack:
            cur = stack.pop()
            print(cur.e)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    def inOrder(self):
        return self._inOrder(self._root)

    def _inOrder(self, node):
        if not node:
            return
        self._inOrder(node.left)
        print(node.e)
        self._inOrder(node.right)

    def postOrder(self):
        return self._postOrder(self._root)

    def _postOrder(self, node):
        if not node:
            return
        self._postOrder(node.left)
        self._postOrder(node.right)
        print(node.e)

    def levelOrder(self):
        queue = deque(self._root)
        while queue:
            cur = queue.popleft()
            print(cur.e)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    def minimum(self):
        if self.isEmpty():
            raise ValueError("BST is empty")
        return self._minimum(self._root).e

    # return node value which has minimum value based on current node
    def _minimum(self, node):
        if not node.left:
            return node 
        return self._minimum(node.left)

    def maximum(self):
        if self.isEmpty():
            raise ValueError("BST is empty")
        return self._maximum(self._root).e

    # return maximum value based on root node
    def _maximum(self, node):
        if not node.right:
            return node 
        return self._maximum(node.right)

    def removeMin(self):
        if self.isEmpty():
            raise ValueError("BST is empty")
        ret = self.minimum()
        self._root = self._removeMin(self._root)
        return ret 

    def _removeMin(self, node):
        # remove minimum node based on current root 
        # the minmum node definitely doesn't have left node
        # return root after remove min node
        if not node.left:
            rightNode = node.right
            node.right = None
            self._size -= 1
            return rightNode

        node.left = self._removeMin(node.left)
        return node 


    def removeMax(self):
        if self.isEmpty():
            raise ValueError("BST is empty")
        ret = self.maximum()
        self._root =  self._removeMax(self._root)
        return ret 

    def _removeMax(self, node):
        # the maximum node definitely doesn't have right node
        # store the node leftnode which can be null or node
        # return node after remove max node
        if not node.right:
            leftNode = node.left
            node.left = None
            self._size -= 1
            return leftNode

        node.right = self._removeMax(node.right)
        return node 

    def remove(self, e):
        self._root = self._remove(self._root, e)

    # return node after finishing remove operation
    def _remove(self, node, e):
        if not node:
            return None 

        # find the node
        if node.e > e:
            node.left = self._remove(node.left, e)
            return node
        elif node.e < e:
            node.right = self._remove(node.right, e)
            return node 
        else: # when node.e == e
            # there are three cases
            # 1. 
            # 3. left and right anode.left is None
            # 2. node.right is Nonere not None 
            if not node.left:
                rightNone = node.right
                node.right = None
                self._size -= 1
                return rightNone 
            if not node.right:
                leftNonde = node.left 
                node.left = None # save memory 
                self._size -= 1
                return leftNonde 
            # when left and right are not None # 找到node右子树的最小值(比node.e大，且离node.e最近的点)
            successor = self._minimum(node.right)
            successor.right = self._removeMin(node.right)
            successor.left = node.left 
            node.left = node.right = None 
            return successor 

    def _generate_depth_string(self, depth):
        res = ""
        for i in range(depth):
            res += '--'
        return res 

    def _generate_BST_string(self, node, depth, res):
        if not node:
            res.append(self._generate_depth_string(depth)+"None\n")
            return 
        res.append(self._generate_depth_string(depth)+str(node.e)+'\n')
        self._generate_BST_string(node.left, depth+1, res)
        self._generate_BST_string(node.right, depth+1, res)

    def __str__(self):
        res = []
        self._generate_BST_string(self._root, 0, res)
        return "BST\n"+ ''.join(res)

    def _repr__(self):
        return self.__str__()

if __name__ == "__main__":
    bst = BST()
    np.random.seed(10)
    for i in range(10):
        a = np.random.randint(50)
        a
        bst.add(a)
    bst.isEmpty()
    bst.size()
    print(bst)
#     bst.inOrder()
#     bst.postOrder()
#     bst.inOrder()
#     bst.removeMax()
#     bst.removeMin()
#     bst.remove(9)
#     print(bst)
# minimum, maximum, sucessor, predecessor, floor, ceil, rank, select,  