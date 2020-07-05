"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        cur = head 
        nxtList = []
        while cur != None:
            if cur.child != None:
                if cur.next != None:
                    nxtList.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            if cur.next == None and cur.child == None and len(nxtList)!=0 :
                cur.next = nxtList.pop()
                cur.next.prev = cur
            cur = cur.next
        return head


