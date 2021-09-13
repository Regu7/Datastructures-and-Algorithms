# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''temp = head
        count = 0
        while temp != None:
            temp = temp.next
            count+=1
        mid =int(count//2) + 1
        for i in range(mid-1):
            head = head.next
        return head '''
        slow = head 
        fast = head
        
        i=0
        
        while fast !=None and fast.next!= None:
            print(i)
            i+=1
            slow = slow.next
            fast = fast.next.next
        return slow
            
        
