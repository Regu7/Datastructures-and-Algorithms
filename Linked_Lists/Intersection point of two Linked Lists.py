# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''tempB = headB
        while headA != None:
            while headB != None:
                if headA == headB:
                    print( headB.val)
                    return headB
                headB = headB.next
            headB = tempB
            headA = headA.next
        return None '''
        
        '''tem1 = headA
        tem2 = headB
        while(headA  != headB):
            
            if headA == None:
                headA = tem2
            else: headA = headA.next
            if headB == None:
                headB = tem1
            else: headB = headB.next      
        return headA '''
            
        visited = set()
        
        while headA:
            visited.add(headA)
            headA = headA.next
        
        while headB:
            if headB in visited:
                return headB
            headB = headB.next
            
            
            
            
            
        
        
        
        
        
