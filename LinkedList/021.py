# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 if l1 else l2
        if l1.val <= l2.val: head,anh = l1,l2
        else: head,anh = l2,l1
        res = head
        while anh:
            if not head.next:
                head.next = anh
                break
            if head.next.val > anh.val:
                head.next,anh = anh,head.next
            head = head.next
        return res

