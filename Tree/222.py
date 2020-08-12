# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None: return 0
        res,i = 0,0
        s = [root]
        while s!= []:
            length = len(s)
            if length < 2 ** i :
                return res + length
            for _ in range(length):
                node = s.pop(0)
                if node.left != None: s.append(node.left)
                if node.right != None: s.append(node.right)
            i += 1
            res += length
        return res