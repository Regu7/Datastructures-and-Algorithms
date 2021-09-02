#Sorting an array
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        #Bubble_sort
        for i in range(len(nums)-1):
            for j in range(len(nums)-1 -i):
                if nums[j+1] < nums[j]:

                     nums[j],nums[j+1] = nums[j+1],nums[j]
                        
        #Dutch_flag_algorithm
        low = 0
        mid = 0
        high = len(nums)-1
        
        while(mid<=high):
            if nums[mid] == 0:
                nums[low],nums[mid] =nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] ==2 :
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
                        
    
        
        
        
