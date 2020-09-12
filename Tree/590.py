"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res,s = [],[root]
        while s: 
            node = s.pop()
            res.append(node.val)
            for child in node.children: s.append(child)
        return res[::-1]

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        for child in root.children: res += self.postorder(child)
        res.append(root.val)
        return res