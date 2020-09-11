# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def helper(root):
            if not root: return 0
            left,right = helper(root.left),helper(root.right)
            tempNode = max(left,right)+1
            tempPath = left+right
            self.res = max(self.res,tempPath)
            return tempNode
        helper(root)
        return self.res