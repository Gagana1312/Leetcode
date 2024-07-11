/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        //split the list from the middle
        // reverse the second list
        // align alternatively

        if(head == null ||head.next==null)return;

        //head if the first half
        ListNode l1 = head;
        //head of the second half
        ListNode slow = head;
        //tail of the second half
        ListNode fast = head;
        //tail of the first half
        ListNode prev=null;

        while (fast != null && fast.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next; // before fast goes twice to last, slow will be in the middle
        }
        prev.next = null; // 1st lists end -> null

        ListNode l2=reverse(slow);

        merge(l1, l2);


        
    }

    public ListNode reverse(ListNode head){

        ListNode prev=null;
        ListNode curr = head;

        while(curr!=null){
            ListNode next_node = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next_node;
        }
        return prev;

    }


    public void merge(ListNode l1, ListNode l2){

        while (l1!=null){
            ListNode l1_next = l1.next;
            ListNode l2_next = l2.next;
            l1.next = l2;
            if (l1_next == null){
                break;
            }
            l2.next = l1_next;
            l1 = l1_next;
            l2 = l2_next;

        }
    }
}