from tools.linked_list import ListNode


class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = home = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            val_sum = v1 + v2 + carry
            val, carry = val_sum % 10, int(val_sum / 10)
            res.next = ListNode(val)
            res = res.next
        return home.next