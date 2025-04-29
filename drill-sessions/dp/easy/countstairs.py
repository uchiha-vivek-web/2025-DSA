
class Solution:
    # recursion
    def reachstairs1(self,n:int):
        if n==0 or n==1:
            return 1
        return self.reachstairs1(n-1) + self.reachstairs1(n-2)
    

    # Tabulation
    # Bottom up
    def reachstairs2(self,n:int):
        if n==0 or n==1:
            return 1
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    
if __name__=="__main__":
    sol=Solution()
    n:int=4
    ans=sol.reachstairs1(n)
    ans1=sol.reachstairs2(n)
    print(ans1)