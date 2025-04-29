

class Solution:
    # recursion
    def countStairs(self,n:int):
        if n==0 or n==1:
            return 1
        
        if n<0:
            return 0

        return self.countStairs(n-1) + self.countStairs(n-2) + self.countStairs(n-3)
    
    # Tabulation
    def countStairsTabulation(self,n:int):
        if n==0 or n==1:
            return 1
        if n<0:
            return 0
        
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]
    
if __name__=="__main__":
    sol=Solution()
    n:int=4
    ans=sol.countStairs(n)
    ans1=sol.countStairsTabulation(n)
    print(ans1)