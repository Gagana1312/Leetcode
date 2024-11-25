# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        
        # Use two pointers to find the middle of the list
        slow, fast = head, head
        prev = None  # To track the node before the middle

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node by skipping it
        if prev:
            prev.next = slow.next

        return head
        