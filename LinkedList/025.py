# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1: return head
        if not head: return head
        node,pre = head,head
        for _ in range(k-1):
            if not node.next: return head 
            node = node.next
        temp = node.next
        cur = pre.next
        for _ in range(k-1):
            nxt = cur.next
            cur.next = pre 
            pre,cur = cur,nxt
        head.next = self.reverseKGroup(temp,k)
        return node