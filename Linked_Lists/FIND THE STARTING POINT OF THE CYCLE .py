# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None :
            return
        
        slow = head
        fast = head
        entry =head
        while(fast.next != None and fast.next.next !=None ):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while(entry != slow):
                    entry = entry.next
                    slow = slow.next
                return entry 
        return 
