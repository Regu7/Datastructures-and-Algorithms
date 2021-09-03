class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ''' c = set()
        for i in nums:
            if i in c:
                return i
            else:
                c.add(i)
        return 0 '''
        hare,tortoise = nums[0],nums[0]
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare ==  tortoise :
                break
        hare = nums[0]
        while hare != tortoise :
            hare = nums[hare]
            tortoise = nums[tortoise]
            
        return hare
            
        
