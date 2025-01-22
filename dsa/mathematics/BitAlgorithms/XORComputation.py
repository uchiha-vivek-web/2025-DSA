"""Compute XOR from 1 to N"""
class Solution :
    def XOR(self,n:int)-> int :
        if n%4 == 0 :
            return n 
        if n%4 == 1:
            return 1
        if n%4 == 2 :
            return n+1
        else :
            return 0

n=4
sol=Solution()
ans = sol.XOR(n)
print(ans)