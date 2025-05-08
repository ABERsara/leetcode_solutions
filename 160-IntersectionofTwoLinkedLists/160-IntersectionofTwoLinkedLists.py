# Last updated: 5/8/2025, 1:18:47 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # check if headA and headB exist 
        # nested while loop to traverse the linked list
        # for each node in list a check if it equals a node in list b
        # if it does then return that node 
        # otherwise keep traversing
        # if it gets to the end then return none
        if not headA or not headB:
            return None

        pointer1, pointer2 = headA, headB

        while pointer1 != pointer2:
            pointer1 = pointer1.next if pointer1 else headB
            pointer2 = pointer2.next if pointer2 else headA

        return pointer1
        