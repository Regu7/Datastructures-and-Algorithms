# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val :
            temp = l1
            l1 = l2
            l2 = temp    
        res = l1
        
        while  (l1 != None and l2 != None):
            temp = ListNode(None)
            while (l1.val <= l2.val and l1 != None):
                temp = l1
                l1 = l1.next
            temp.next = l2
            tmp = l1
            l1 =l2
            l2 =tmp   
        return res
            
#The above one is with o(1) space but its not working below is with o(n) space
        
       
        ''' newnode = ListNode(0)
        head = newnode
        
        while True:
            if l1 == None:
                newnode.next = l2
                break
            if l2 == None:
                newnode.next = l1
                break
            if l1.val <= l2.val :
                newnode.next =l1 
                newnode = newnode.next
                l1 = l1.next   
            elif l2.val < l1.val :
                newnode.next = l2
                newnode = newnode.next
                l2 =l2.next          
        return head.next  '''
                
                
        
