from tools.linked_list import ListNode

def delete_duplicates(head):
    slow = fast = head
    if not head:
        return head
    while fast:
        if fast.val != slow.val:
            slow.next = fast
            slow = fast
            fast = slow.next
        else:
            fast = fast.next
    slow.next = fast
    return head
