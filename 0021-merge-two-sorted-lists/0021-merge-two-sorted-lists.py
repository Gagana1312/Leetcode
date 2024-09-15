# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # newHead = ListNode()
        # curr = newHead
        # if not list1:
        #     return None
        # if not list2:
        #     return None
        # while list1 and list2:
        #     temp1 = list1.next
        #     temp2 = list2.next
        #     curr.next = list1
        #     curr.next.next= list2
        #     list1 = temp1
        #     list2 = temp2
        #     curr = curr.next.next
        # if list1:
        #     curr.next = list1
        # elif list2:
        #     curr.next = list2
        # return newHead.next

        d = ListNode()
        cur = d
        while list1 and list2:
            if list1.val <list2.val:
                cur.next= list1
                cur = list1
                list1=list1.next
            else:
                cur.next= list2
                cur = list2
                list2=list2.next
        cur.next = list1 if list1 else list2
        return d.next
        



            


        