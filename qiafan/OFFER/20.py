# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def theSameTree(T1, T2):
            if T2 == None:
                return True
            if T1 == None:
                return False
            if T1.val == T2.val:
                return True and theSameTree(T1.left,T2.left) and theSameTree(T1.right, T2.right)
            return False

        if not A and not B:
            return True
        if not A or not B:
            return False
        s = [A]
        while s:
            node = s.pop()
            if node.val == B.val:
                if theSameTree(node, B): return True
            if node.left: s.append(node.left)
            if node.right: s.append(node.right)
        return False