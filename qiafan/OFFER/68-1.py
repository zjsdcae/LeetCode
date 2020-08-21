# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def SearchPath(root,tar):
#             temp,res = root,[]
#             while temp.val != tar.val:
#                 res.append(temp)
#                 if temp.val < tar.val: root = root.right
#                 if temp.val > tar.val: root = root.left
#                 temp = root
#             res.append(root)
#             return res
#         pPath = SearchPath(root, p)
#         qPath = SearchPath(root, q)
#         idx,length = 0,min(len(pPath),len(qPath))
#         while idx < length:
#             if pPath[idx] == qPath[idx]: idx += 1
#             else: break
#         return qPath[idx-1]

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p,q = q,p
        while root:
            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                return root