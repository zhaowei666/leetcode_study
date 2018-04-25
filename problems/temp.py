fast = slow = head
n = 1
if not fast:
    return head
while fast.next:
    n += 1
    fast = fast.next
k = k % n
if k == 0:
    return head
fast = head
for i in range(k):
    fast = fast.next
while fast.next:
    fast = fast.next
    slow = slow.next
fast.next = head
res = slow.next
slow.next = None
return res
