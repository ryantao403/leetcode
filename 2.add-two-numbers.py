#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = l1, l2
        dummy = ListNode()
        curr = dummy
        carry = 0
        while p or q:
            num = carry
            if p:
                num += p.val
                p = p.next
            if q:
                num += q.val
                q = q.next
            carry = num // 10
            num = num % 10
            curr.next = ListNode(num)
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next
# @lc code=end

