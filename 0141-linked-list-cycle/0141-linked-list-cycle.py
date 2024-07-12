# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        # curr = head
        # arr = []
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next
        #     if curr is None:
        #         return False
        #     if curr.val in arr:
        #         return True
        # return False


        

