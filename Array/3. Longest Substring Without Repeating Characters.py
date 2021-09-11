class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longstreak = 0
        s_set = {}
        l,r = 0,0
        n = len(s)
        
        
        while(r<n):
                if s[r]  in s_set.keys():
                    l = max(s_set[(s[r])] +1,l)
                    
                s_set[s[r]] = r
                tempcount = r-l+1 
                longstreak = max(tempcount,longstreak)
                r+=1 
                    
                    
                    
                
                    
                    
                    
            
        return longstreak
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longstreak = 0
        s_set = set()
        l,r = 0,0
        n = len(s)
        
        while(l<=r and r<n):
                if s[r] not in s_set:
                    s_set.add(s[r])
                    tempcount = r-l+1 
                    longstreak = max(tempcount,longstreak)
                    r+=1 
                else:
                    s_set.discard(s[l])
                    l+=1 
            
        return longstreak
                    
                
                
                       
                       
                       
                       
                       
                       
                       
                       
                  
                       
                       
            
                       
                       
                
           
        
