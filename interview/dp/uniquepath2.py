from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # first principal thinking --> fill all rows and columns with 1 and 1
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        # if starting cell or ending cell is blocked 
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1]==1:
            return 0
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1
        
        # filling the columns
        for i in range(1,m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=dp[i-1][0]
        
        # filling the rows
        for j in range(1,n):
            if obstacleGrid[0][j]==0:
                dp[0][j] = dp[0][j-1]
        
        # filling the rest of the table
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
        
        
        
if __name__=="__main__":
    sol=Solution()
    obstacleGrid:List[List[int]] = [[0,0,0],[0,1,0],[0,0,0]]
    ans = sol.uniquePathsWithObstacles(obstacleGrid)
    print(ans)



# upcoming problems
# unique path 3
# path whose matrix sum is divisible by 3