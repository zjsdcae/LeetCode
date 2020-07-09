# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i,p = 1,head
        while i < m:
            p = p.next
            i += 1
        q = p 
        j = 1
        while j < n-m :
            q.