/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode SwapPairs(ListNode head) {
        ListNode temp,result=head,prev=null;
        while(head!=null && head.next!=null){
            temp=head;
            head=head.next;
            temp.next=head.next;
            head.next=temp;
            if(prev==null){
                result=head;
            }
            else{
                prev.next=head;
            }
            head=temp.next;
            prev=temp;
        }
        return result;
    }
}
