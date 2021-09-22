class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        num.sort()
        l = []
        for i in range(0,len(num)-2):
            
            if ( i == 0 or ( num[i]!= num[i-1] and i > 0)):
                
                low = i+1
                hi = len(num) - 1 
                summ = 0 - num[i]
                
                while(low < hi):
                    if num[low] + num[hi] ==  summ :
                        print('hi')
                        l.append([num[i],num[low],num[hi]])

                        while(low < hi  and num[low] == num[low+1]):low+=1
                        while(low < hi and num[hi] ==  num[hi-1]): hi-=1
                        low+=1
                        hi -=1
                    else:
                        if num[low] + num[hi] < summ : low+=1
                        else: hi-=1
        return l
                        
                        
                
                    
                
                
        
