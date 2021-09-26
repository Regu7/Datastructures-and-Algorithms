class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ''' nums = [1,1,2]
Output: 2, nums = [1,2,_]'''
        n = len(nums)
        i = 0 
        j =1
        while(j< n):
            if nums[i] == nums [j]:
                j+=1
            else:
                i+=1
                nums[i] = nums[j]
                j+=1
        print(nums)
        return i+1
