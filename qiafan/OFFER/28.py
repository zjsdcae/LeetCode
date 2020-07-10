# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def judge(l, r):
            if not l and not r: return True
            if not l or not r or l.val != r.val: return False
            return judge(l.left, r.right) and judge(l.right, r.left)
        judge(root.left, root.right)