# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def bfs(node):
            if node == None:
                return 0
            left = bfs(node.left)
            if left == -1: 
                return -1
            right = bfs(node.right)
            if right == -1:
                return -1
            return max(left,right)+1 if abs(left-right) <= 1 else -1
        return bfs(root) != -1

# class Solution:
#     def bfs(self, node):
#         if node == None:
#             return 0
        
#         l = self.bfs(node.left)+1
#         r = self.bfs(node.right)+1
#         if l-r > 1:
#             return inf
#         return max(l,r)

#     def isBalanced(self, root: TreeNode) -> bool:
#         if root == None:
#             return True
#         return abs(self.bfs(root.left)-self.bfs(root.right)) < 2
