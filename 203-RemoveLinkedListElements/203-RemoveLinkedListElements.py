# Last updated: 5/13/2025, 2:19:55 PM
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head

        curr = dummy

        while curr.next != None and curr != None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next

        