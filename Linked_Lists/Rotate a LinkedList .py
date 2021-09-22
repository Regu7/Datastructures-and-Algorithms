# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        count = 1
        if head == None or head.next == None:
            return head
        
        while(temp.next != None):
            count+=1
            temp = temp.next
        print(count)
        k = k % count
        k = count - k 
        temp.next = head
        #temp = temp.next
        while(k > 0):
            k-=1
            temp = temp.next
        cur = temp.next
        temp.next = None
        return cur
