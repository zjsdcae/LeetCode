# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l,r = 0,0
        if root.left:
            l = self.maxDepth(root.left)
        if root.right:
            r = self.maxDepth(root.right)
        return max(l,r)+1