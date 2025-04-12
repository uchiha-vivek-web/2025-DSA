

class Solution :
    def ValidPerfectSquare(self,num:int):
        # O(sqrt(N))
        for i in range(1,num+1):
            if i*i == num :
                return True
            if i*i > num:
                return False
            
    def ValidPerfectSquareBinarySearch(self,num:int):
        # Time complexity : O(logN)
        l,r = 1, num
        while l<=r :
            mid = (l+r)//2
            if mid*mid > num :
                r=mid-1
            elif mid*mid < num:
                l=mid+1
            else:
                return True
        return False
    
sol=Solution()
num=9
ans=sol.ValidPerfectSquareBinarySearch(num)
print(ans)