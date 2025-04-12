
""" Time Complexity : O(NlogN) """

class Solution:
    def splitArray(self,nums:list[int],m:int)-> int:
        def canSplit(largest):
            subarray=0
            curSum=0
            for n in nums:
                curSum+=n
                if curSum>largest:
                    subarray+=1
                    curSum=n
            return subarray + 1 <=m
        l,r = max(nums),sum(nums)
        res = r
        while l<=r:
            mid=(l+r)//2
            if canSplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res


sol=Solution()
nums=[7,2,5,10,8]
k=2
ans=sol.splitArray(nums,k)
print(ans)