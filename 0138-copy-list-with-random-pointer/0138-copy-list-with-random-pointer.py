"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # oldToCopy ={None: None}
        # curr = head
        # #create the copy of the nods first.
        # while curr:
        #     copy =Node(curr.val)
        #     oldToCopy[curr]=copy
        #     curr=curr.next
        # curr=head
        # #connect the points to the copied nodes.
        # while curr:
        #     copy = oldToCopy[curr]
        #     copy.next = oldToCopy[curr.next]
        #     copy.random = oldToCopy[curr.random]
        #     curr=curr.next
        
        # return oldToCopy[head]

        if not head: return None
        curr = head
        oldtonew ={}

        while curr:
            node= Node(x=curr.val)
            oldtonew[curr]=node
            curr=curr.next
        curr=head

        while curr:
            newnode=oldtonew[curr]
            newnode.next=oldtonew[curr.next] if curr.next else None
            newnode.random=oldtonew[curr.random] if curr.random else None
            curr=curr.next
        return oldtonew[head]