# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''   
        i = 0
        temp  =  head 
        res = head
        prev = None
        while head != None :
            i+=1
            head = head.next
        if i == 1:
            return 
        m = i-n
        if m==0:
            return temp.next
        for i in range(m):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return res '''
        
        start = ListNode()
        start.next = head 
        slow = start
        fast = start
        for i in range(1,n+1):
            fast  = fast.next
        while(fast.next!= None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return start.next
        
            
        
