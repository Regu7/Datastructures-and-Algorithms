# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''remainder = 0
        temp = ListNode(5)
        head = temp
        while l1 != None or l2!= None:
            if l1!= None and l2 == None:
                a = l1.val + remainder
                l1 = l1.next
            elif l2!= None and l1 == None:  
                a = l2.val + remainder
                l2 = l2.next
            else:
                a = l1.val + remainder + l2.val
                l1 = l1.next
                l2 = l2.next 
            remainder = a//10
            a = a % 10
            temp.next = ListNode(a)
            temp = temp.next    
        if remainder != 0:
            temp.next = ListNode(remainder)
        return head.next ''' 
    
    
        ret = ListNode()
        ret.val=0
        
        tmp = ret
        
        adder = 0
        while True:
            s = 0
            s+= adder
            if l1 != None:
                s+=l1.val
                l1 = l1.next
            if l2 != None:
                s+=l2.val
                l2 = l2.next
            tmp.val=s%10
            adder = s// 10
            
            if l1 == None and l2 == None and adder == 0:
                break
                
            tmp.next = ListNode()
            tmp=tmp.next
            
        return ret
            
            
