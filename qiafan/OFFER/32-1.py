# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        s = [root]
        res = []
        while s:
            length = len(s)
            for _ in range(length):
                node = s.pop(0)
                res.append(node.val)
                if node.left: s.append(node.left)
                if node.right: s.append(node.right)
        return res