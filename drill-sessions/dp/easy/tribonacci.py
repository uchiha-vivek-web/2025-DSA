

# Designing tribonacci

class Solution:
    # tribonaci using recursion
    def tribonacirecursion(self,n:int):
        # a(0)=0 , a(1)=0 , a(2)=1
        if n<=1:
            return 0
        if n==2:
            return 1
        return self.tribonacirecursion(n-1) + self.tribonacirecursion(n-2) + self.tribonacirecursion(n-2)
    

if __name__=="__main__":
    sol=Solution()
    n:int=4
    ans=sol.tribonacirecursion(5)
    print(ans)