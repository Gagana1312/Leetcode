# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        # Recursive solution
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next= head
        # head.next = None
        # return newHead

        # Iterative

        prev= None
        curr= head
        while curr:
            temp = curr.next
            curr.next= prev
            prev= curr
            curr= temp
        return prev

        



        