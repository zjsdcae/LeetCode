# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution: 
    def levelOrder(self, root):
        res = []
        if root == None:
            return []
        def dfs(index, node):
            if len(res) < index:
                res.append([])
            res[index-1].append(node.val)
            if node.left:
                dfs(index+1, node.left)
            if node.right:
                dfs(index+1, node.right)
        dfs(1,root)
        return res

        # res = []
        # if root == None:
        #     return [[]]
        # s = [root]
        # s2 = []
        # while s or s2:
        #     layer = []
        #     for node in s:
        #         layer.append(node)
        #         if node.left:
        #             s2.append(node.left)
        #         if node.right:
        #             s2.append(node.right)
        #     s = []
        #     res.append(layer)
        #     layer = []
        #     for node in s2:
        #         layer.append(node)
        #         if node.left:
        #             s.append(node.left)
        #         if node.right:
        #             s.append(node.right)
        #     s2 = []
        #     res.append(layer)
        # return res            