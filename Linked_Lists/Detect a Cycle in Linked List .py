# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        if head is None:
            return False
        while(fast != None and fast.next!=None ):
             
            
            
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
            
        
