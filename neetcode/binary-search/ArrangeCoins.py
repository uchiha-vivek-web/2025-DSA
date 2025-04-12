

class Solution:
    def arrangeCoins(self,n:int):
        # Time complexity :O(N) 
        row=0
        while n>=row+1:
            row+=1
            n-=row
        return row
    

    def arrangeCoinsBS(self,n:int):
        # Time complexity O(log(N))
        l,r = 1, n
        res=0

        while l<=r:
            mid = (l+r)//2
            coins = (mid/2)*(mid+1)
            if coins > n:
                r=mid-1
            else:
                l=mid+1
                res=max(mid,res)
            
        return res


sol=Solution()
n=5
ans=sol.arrangeCoins(n)
ans1=sol.arrangeCoinsBS(n)
print(ans1)