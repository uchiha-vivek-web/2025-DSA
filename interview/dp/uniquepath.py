# https://leetcode.com/problems/unique-paths/?envType=problem-list-v2&envId=dynamic-programming


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for  i in range(m):
            row = []
            for j in range(n):
                if i==0 or j==0:
                    row.append(1)
                else : 
                    row.append(0)
            dp.append(row)
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]