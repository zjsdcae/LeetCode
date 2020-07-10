# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = None
        while head.next != None:
            cur = head 
            head = head.next
            cur.next = node
            node = cur
        return head
        # cur, prev = head, None
        # while cur:
        #     cur, cur.next, prev = cur.next, prev, cur
        # return prev