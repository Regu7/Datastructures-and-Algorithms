
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        second=lambda x:x[1]
        interval=list(zip(start,end))
        interval.sort(key=second)
        count =1
        endi =interval[0][1]
        for i in range(1,n):
            if interval[i][0]>=endi+1:
                count+=1
                endi=interval[i][1]
        return count  

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
