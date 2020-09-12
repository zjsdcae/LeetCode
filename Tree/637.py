# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res,s = [],[root]
        while s:
            temp = []
            length = len(s)
            for _ in range(length): 
                node = s.pop(0)
                temp.append(node.val)
                if node.left: s.append(node.left)
                if node.right: s.append(node.right)
            res.append(sum(temp)/len(temp))
        return res

