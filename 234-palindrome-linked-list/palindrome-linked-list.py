# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        store = []
        current = head
        while current:
            store.append(current.val)
            current = current.next
        left = 0
        right = len(store) - 1
        while left < right:
            if store[left] != store[right]:
                return False
            left += 1
            right -= 1
        return True