# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        low = head
        fast = head
        for _ in range(1,k):
            fast = fast.next
        while fast.next != None:
            low = low.next
            fast = fast.next
        return low