# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        d= ListNode(0)
        d.next= head
        slow = d
        fast = d
        i=0
        while i<n:
            fast = fast.next
            i+=1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next= slow.next.next
        return d.next
                
        
        