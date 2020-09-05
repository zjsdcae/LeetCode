# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        head = root
        while head:
            if head.val > val: 
                if not head.left:
                    head.left = TreeNode(val)
                    return root
                else: head = head.left
            elif not head.right:
                head.right = TreeNode(val)
                return root
            else: head = head.right
        return root