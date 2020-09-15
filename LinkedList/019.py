# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        p,q = temp,temp 
        for _ in range(n): q = q.next 
        while q and q.next:
            q = q.next
            p = p.next 
        p.next = p.next.next 
        return temp.next