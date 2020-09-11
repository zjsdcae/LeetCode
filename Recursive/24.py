# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        temp = head.next.next
        nxt = head.next
        nxt.next = head
        head.next = self.swapPairs(temp)
        return nxt