# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k ==1 or head == None:
            return head
        dummy = ListNode(0) 
        dummy.next = head
        cur = dummy
        nextt = dummy 
        prev = dummy
        count = 0
        while(head != None):
            head = head.next
            count+=1
        while (count >= k):
            cur = prev.next
            nextt = cur.next
            for i in range(1,k):
                cur.next = nextt.next
                nextt.next = prev.next
                prev.next = nextt
                nextt = cur.next
            prev = cur
            count-=k
        return dummy.next
                
        
