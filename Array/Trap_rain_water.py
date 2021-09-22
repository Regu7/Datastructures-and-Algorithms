class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        i = 0
        r = n-1
        res = 0
        lmax = 0
        rmax = 0
        while(l<=r):
            if height[l]<=height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    res+= (lmax-height[l])
                l+=1
                    
            else:
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    res+=(rmax-height[r])
                r-=1
        return res
        
        
