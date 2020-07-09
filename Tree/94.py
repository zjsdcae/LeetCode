# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if root == None:
#             return res
#         res += self.inorderTraversal(root.left)
#         res.append(root.val)
#         res += self.inorderTraversal(root.right)
#         return res

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root
        if root == None:
            return res
        s = []
        while s or cur:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            res.append(cur.val)
            cur = cur.right
        return res