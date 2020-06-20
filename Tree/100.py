class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if !p or !q:
            return !p and !q
        elif p.val == q.val:
            return  True and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
