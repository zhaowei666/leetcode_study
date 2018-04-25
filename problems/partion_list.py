class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):
    pre = small = ListNode(0)
    large = large_pre = ListNode(0)
    while head:
        if head.val < x:
            small.next = head
            small = small.next
        else:
            large.next = head
            large = large.next
        head = head.next
    small.next = large_pre.next
    large.next = None
    return pre.next

a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(3)
a4 = ListNode(2)
a5 = ListNode(5)
a6 = ListNode(2)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6

res = partition(a1, 3)
while res:
    print(res.val)
    res = res.next