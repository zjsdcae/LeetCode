class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        length = len(postorder)
        if length < 2:
            return True
