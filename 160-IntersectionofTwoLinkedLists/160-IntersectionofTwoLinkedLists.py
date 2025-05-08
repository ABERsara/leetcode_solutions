# Last updated: 5/8/2025, 1:11:17 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB

        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a
