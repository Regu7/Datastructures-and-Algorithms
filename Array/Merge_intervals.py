  def merge(self, a: List[List[int]]) -> List[List[int]]:
        out = []
        a.sort()  
        cur =a[0]
        if len(a) == 0:
            return out
        for i in a:
            if i[0] <= cur[1]:
                cur[1] = max(cur[1],i[1])  
            else:
                out.append(cur)
                cur = i
        out.append(cur)
        return out
