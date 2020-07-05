# LinkedList Notes

### reverse linked list 
```python 
cur = head
pre = None
while cur:
    nxt = cur.next
    cur.next = pre
    pre = cur
    cur = next
return pre
```

### merge linked list 
```python 
ans = new Node(-1)
cur = ans
while l1 and l2:
    cur.next = min(l1.val, l2.val)
    if l1 == null:
        cur.next = l2
    if l2 == null:
        cur.next = l1
    return ans.next
```

