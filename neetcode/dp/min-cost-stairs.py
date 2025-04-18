
class Solution:
    def mincostofclimbing(self,cost:list[int]):
        """
        Space complexity : O(N)
        Time complexity : O(1)
        """

        n=len(cost)
        if n==0:
            return 0
        if n==1:
            return cost[1]
        
        dp=[0]*n
        dp[0]=cost[0]
        dp[1]=cost[1]

        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        
        return min(dp[-1],dp[-2])
    
    """ optimization in dp """
    """
    Time complexity : O(N)
    Space complexity : O(1)
    """
    def mincostarrayoptimizedbyspace(self,cost:list[int]):
        a = cost[0]
        b = cost[1]
        for i in range(2,len(cost)):
            a,b = b , cost[i] + min(a,b)
        return min(a,b)


if __name__=="__main__":
    sol=Solution()
    nums=[10,15,20]
    sol = sol.mincostofclimbing(nums)
    print(sol)