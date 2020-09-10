# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None: return head
        pre0 = ListNode(0)
        pre0.next = head
        pre = pre0
        for _ in range(1,m): pre = pre.next
        cur = pre.next
        node,nxtnode = cur,cur.next
        for _ in range(n-m):
            temp = nxtnode.next
            nxtnode.next,node = node,nxtnode
            nxtnode = temp
        pre.next = node
        cur.next = nxtnode
        return pre0.next
