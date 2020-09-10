# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        node,nxt = head,head.next
        while nxt:
            if nxt.val == node.val: nxt = nxt.next
            else: 
                node.next = nxt
                node = nxt
                nxt = node.next
        node.next = nxt
        return head
