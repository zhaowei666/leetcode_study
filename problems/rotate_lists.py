from tools.linked_list import ListNode


def rotate_right(head, k):
    cur = head
    n = 0
    while cur:
        n += 1
        cur = cur.next
    if n == 0:
        return head
    k = k % n
    if k == 0:
        return head
    fast = slow = home = ListNode(0)
    fast.next = slow.next = home.next = head
    for i in range(k):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    home.next = slow.next
    slow.next = None
    fast.next = head
    return home.next
