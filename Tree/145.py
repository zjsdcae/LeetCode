# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if root == None:
#             return res
#         res.extend(self.postorderTraversal(root.left))
#         res.extend(self.postorderTraversal(root.right))
#         res.append(root.val)
#         return res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res
        s = [root]
        while s :
            node = s.pop()
            res.append(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return res[::-1]