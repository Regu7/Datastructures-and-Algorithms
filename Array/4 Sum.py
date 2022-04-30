class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = list()
        if n == 0 :
            return res
        res = list()
        nums.sort()
        print(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                front = j+1
                back = n-1
                diff = target - nums[i] - nums[j]
                while front < back :
                    
                    twosum = nums[front] + nums[back]
                    if twosum < diff : front+=1
                    elif twosum > diff : back-=1
                    else:
                        quad = list([])
                        quad.append(nums[i])
                        quad.append(nums[j])
                        quad.append(nums[front])
                        quad.append(nums[back])
                        res.append(tuple(quad))
                        while front < back and nums[front] == quad[2]:
                            front+=1
                        while front < back and nums[back] == quad[3]:
                            back-=1
                while (j+1 < n and nums[j] == nums[j+1]):j+=1
            while (i+1 < n and nums[i] == nums[i+1]):i+=1
                   
                        
        return set((res))
                            
'''             
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
	
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            
            # If we have run out of numbers to add, return res.
            if not nums:
                return res
            
            # There are k remaining values to add to the sum. The 
            # average of these values is at least target // k.
            average_value = target // k
            
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest 
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            if k == 2:
                return twoSum(nums, target)
    
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
    
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
    
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
    
            return res

        nums.sort()
        return kSum(nums, target, 4)
''' 
