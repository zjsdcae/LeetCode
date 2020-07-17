# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def bfs(root, minF, maxF):
            if root == None:
                return True
            if not minF < root.val < maxF:
                return False
            return True and bfs(root.left, minF, root.val) and bfs(root.right, root.val, maxF)
        return bfs(root, -inf, inf)

