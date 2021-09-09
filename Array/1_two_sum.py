class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j] '''
        has = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff not in has.keys():
                has[nums[i]] = i
            else:
                return has[diff],i
            
                    
  
