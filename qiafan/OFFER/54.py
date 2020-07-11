# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def traverse(node):
            if node == None:
                return
            res = []
            if node.left:
                res += traverse(node.left)
            res.append(node)
            if node.right:
                res += traverse(node.right)
            if node.left == None and node.right == None:
                return [node]
            return res
        s = traverse(root)
        for _ in range(k):
            temp = s.pop()
        return temp.val