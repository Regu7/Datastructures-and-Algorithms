ef maxProfit(self, a: List[int]) -> int:
        n =  len(a)
        maxprof = 0
        mini = max(a)+1
        for i in range(n):
            mini = min(mini,a[i])
            maxprof = max(maxprof , a[i] - mini )
            
        return maxprof
