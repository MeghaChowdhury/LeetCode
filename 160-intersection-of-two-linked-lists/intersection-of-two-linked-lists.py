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
        pa = headA
        pb = headB

        while pa != pb:
            
            if pa == None:
                pa = headB
            else:
                pa = pa.next
            if pb == None:
                pb = headA
            else:
                pb = pb.next
        return pa
            
        