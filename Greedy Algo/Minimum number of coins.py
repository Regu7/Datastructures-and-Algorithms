class Solution:
	
		def minCoins(self, coins, M, V):
		# code here
    		num = 0
    		for i in coins:
    		    #print(V,i)
    		    if V >= i:
    		         num += V//i
    		         V = V%i
		
		    return num
