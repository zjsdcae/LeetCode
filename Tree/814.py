# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def judge(node):
            if node == None:
                return False
            if node.val == 1:return True
            else: 
                if node.left or node.right:
                    return False or judge(node.left) or judge(node.right)
        if root == None:
            return None
        s = [root]
        while s:
            cur = s.pop()
            if cur.left: 
                if judge(cur.left): s.append(cur.left)
                else: cur.left = None
            if cur.right:
                if judge(cur.right): s.append(cur.right)
                else: cur.right = None
        return root
