# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def searchNode(root, l, num):
            if root.val == num and root.left == None and root.right == None: 
                res.append(l + [root.val])
            else:
                if root.left: searchNode(root.left, l+[root.val], num-root.val)
                if root.right: searchNode(root.right, l+[root.val], num-root.val)
            return

        if root == None:
            return []
        searchNode(root, [], sum)
        return res