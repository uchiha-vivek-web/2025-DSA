

class Solution:
    """
    Time complexity : O(N) 
    Space complexity : O(N) Each recursive call add a new frame to call stack
    """
    def sum(self,n:int):
        if n==0:
            return 0
        return n + self.sum(n-1)
    

if __name__=="__main__":
    sol=Solution()
    n=5
    ans=sol.sum(n)
    print(ans)