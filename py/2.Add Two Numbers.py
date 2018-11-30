# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        curr = head
        
        p, q = l1, l2
        while p or q:
            total = carry
            if p:
                total += p.val 
                p = p.next
            if q:
                total += q.val
                q = q.next
            curr.next = ListNode(total % 10)
            carry = total // 10
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return head.next