"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        res = []
        s = [root]
        while s:
            node = s.pop(0)
            res.append(node.val)
            if node.children:
                s = node.children+s
        return res