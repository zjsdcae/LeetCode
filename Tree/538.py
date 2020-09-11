# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        s,node,temp = [],root,[]
        while node or temp:
            if node:
                temp.append(node)
                node = node.left        
            else: 
                node = temp.pop()
                s.append(node)
                node = node.right
        for i in range(len(s)-2,-1,-1):
            s[i].val += s[i+1].val 
        return root