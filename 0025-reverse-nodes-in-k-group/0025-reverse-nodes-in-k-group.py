# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        groupPrev = dummy
        while True:
            kth = self.getkth(groupPrev,k)
            if not kth:
                break
            groupNext= kth.next

            #reversing the group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev=curr
                curr=tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev= tmp
        return dummy.next


    def getkth(self, curr, k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
        