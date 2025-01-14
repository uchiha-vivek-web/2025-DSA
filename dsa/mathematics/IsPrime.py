import math
class Solution : 
    def isPrime(self,n:int)->bool :
        if n<=1:
            return False
        for i in range(2,n):
            if n % i == 0 : return False
            return True
    def isPrimeSqrt(self,n:int)-> bool :
        if n<=1 :
            return False
        num_sqrt = math.sqrt(n)
        for i in range(2,int(num_sqrt)+1):
            if n %i==0 : return False
            return True
    def ModifiedSqrt(self,n:int)-> bool :
        if n==2 or n==3 :
            return True
        elif n<=1 or n%2==0 or n%3==0:
            return False
        for i in range(5,int(math.sqrt(n))+1,6):
            if n % i ==0 or n % (i+2) ==0:
                return False
            return True
        

n=8
sol = Solution()
ans = sol.isPrime(n)
ans1 = sol.isPrimeSqrt(n)
print(ans,ans1)