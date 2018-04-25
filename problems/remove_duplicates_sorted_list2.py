class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_duplicates(head):
    slow = pre = ListNode(0)
    pre.next = slow.next = None
    if not slow:
        return head
    fast = head
    if not fast:
        return head
    v = None
    while fast.next:
        if v != fast.val:
            if fast.val != fast.next.val:
                slow.next = fast
                slow = fast
        v = fast.val
        fast = fast.next
    if fast.val != v:
        slow.next = fast
        slow = fast
    slow.next = None
    return pre.next


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(2)
a1.next = a2
a2.next = a3
res = remove_duplicates(a1)
while res:
    print(res.val)
    res = res.next


