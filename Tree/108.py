# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        idx = len(nums)//2
        node = TreeNode(nums[idx])
        node.left = self.sortedArrayToBST(nums[:idx])
        node.right = self.sortedArrayToBST(nums[idx+1:])
        return node