def remove_nth_node(head, n):
    slow = fast = cur = ListNode(0)
    slow.next = fast.next = cur.next = head
    for i in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return cur.next