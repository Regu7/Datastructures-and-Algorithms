class Solution:
    def reversePairs(self, nums: List[int]) -> int:
    
            
        def mergesort(arr,low,mid,high):
            count = 0
            
            j = mid+1
            for i in range(low,mid+1):
                while ( j <= high and arr[i] > 2* arr[j]):
                    j+=1
                count += (j-(mid+1))
            left = low
            right =  mid+1
            temp = []
            while (left <= mid and right<= high):
                    if arr[left] <= arr[right]:
                        temp.append(arr[left])
                        left+=1
                        
                    else:
                        temp.append(arr[right])
                        right+=1
            while(left<= mid):
                temp.append(arr[left])
                left+=1
            while(right <= high):
                temp.append(arr[right])
                right+=1
            
            for i in range(low,high+1):
                arr[i] = temp[i-low]
            return count        
        def merge(arr , low ,high):
            
            if low>=high : 
                return 0
            mid = (low + high) // 2
            inv = merge(arr,low,mid)
            inv += merge(arr,mid+1,high)
            inv += mergesort(arr,low,mid,high)
            return inv
        return(merge(nums,0,len(nums)-1))
        
