class Solution:
    def climbstairs(self,n:int):
        def dfs(current:int):
            if current == n:
                return 1
            if current > n:
                return 0
            return dfs(current+1) + dfs(current+2)
        return dfs(0)
    
    
    """with memoization"""
    def climbstairsmemo(self,n:int):
        memo={}
        def dfs(current:int):
            if current==n:
                return 1
            if current > n:
                return 0
            if current in memo :
                return memo[current]
            memo[current] = dfs(current+1) + dfs(current+2)
            return memo[current]
        return dfs(0)
           
    def climbstairsdp(self,n:int):
        one,two=1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        
        return one
    






if __name__=='__main__':
    sol=Solution()
    n:int=5
    ans = sol.climbstairs(n)
    ans1=sol.climbstairsmemo(n)
    ans2 = sol.climbstairsdp(n)
    print(ans2)