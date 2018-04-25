slow = pre = ListNode(0)
slow.next = None
cur = head
pre = slow
if not cur:
    return head
while cur.next:
    fast = cur.next
    is_unique = True
    while cur.val == fast.val:
        if fast.next:
            fast = fast.next
        else:
            slow.next = None
            return pre.next
        is_unique = False
    if is_unique:
        slow.next = cur
        slow = cur
    cur = fast
if cur:
    slow.next = cur
return pre.next