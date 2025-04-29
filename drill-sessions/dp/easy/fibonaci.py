
class Solution:
    # using recursion
    # Time complexity : O(2^N) and space complexity : O(N)
    def fibonacirecursion(self,n:int):
        if n<=1:
            return n
        return self.fibonacirecursion(n-1) + self.fibonacirecursion(n-2)
    

    # Bottom up approach
    # Tabulation
    def fibonicibottomup(self,n:int):
        # Time complexity : O(N)
        # space complexity : O(N)
        # edge case
        if n<=1:
            return n
        
        # list to store fibonaci series
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]

    # Memoization
    # Top to down approach
    def fibonacitopdown(self,n,memo={}):
        # Time complexity: O(N)
        # space complexity : O(N)
        if n in memo:
            return memo[n]
        # base case
        if n<=1:
            return n
        memo[n] = self.fibonacitopdown(n-1,memo) + self.fibonacitopdown(n-2,memo)
        return memo[n]


    # swap technique
    


if __name__=="__main__":
    sol=Solution()
    n=4
    ans=sol.fibonacirecursion(n)
    ans1=sol.fibonicibottomup(n)
    ans2=sol.fibonacitopdown(n)
    print(ans2)