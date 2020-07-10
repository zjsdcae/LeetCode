# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        s = [root]
        while s:
            node = s.pop()
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
            node.left, node.right = node.right, node.left       
        return root
        # root.left, root.right = root.right, root.left
        # self.mirrorTree(root.left)
        # self.mirrorTree(root.right)
        # return root