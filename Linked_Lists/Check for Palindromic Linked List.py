# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            cur =  head
            a = []
            prev = None
            #5-4-3-2
            while cur != None:
                next = cur.next #4
                cur.next = prev #None
                prev = cur #5
                cur = next #4
            head = prev
            return head
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        temp = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        prev = slow.next
        cur = slow.next  
        slow.next =  self.reverseList(slow.next)
        slow = slow.next
        while(slow!= None):
            if slow.val != temp.val :
                return False
            slow = slow.next
            temp = temp.next
        return True
            
        
        
            
            
        
