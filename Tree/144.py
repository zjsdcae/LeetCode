# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if root is None:
#             return res
#         res.append(root.val)
#         res += self.preorderTraversal(root.left)
#         res += self.preorderTraversal(root.right)
#         return res

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res
        s = []
        s.append(root)
        while s :
            node = s.pop()
            res.append(node.val)
            if node.right :
                s.append(node.right)
            if node.left :
                s.append(node.left)
        return res
