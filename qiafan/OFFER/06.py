# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        s,res = [],[]
        while head != None:
            s.append(head.val)
            head = head.next
        while s != []:
            res.append(s.pop())
        return res
        # return s[::-1]