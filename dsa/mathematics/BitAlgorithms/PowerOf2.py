"""Function to know whether a number is power of 2 or not .  """
class Solution :
    def isPowerOfTwo(self,n:int):
        if n==0 :
            return n
        return n&(n-1)

sol=Solution()
n=3
ans=sol.isPowerOfTwo(n)
print(ans)