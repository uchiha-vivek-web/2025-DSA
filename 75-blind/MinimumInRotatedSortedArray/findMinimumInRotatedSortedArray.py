


class Solution:
    def findMinimumInRotatedSortedArray(self,nums:list[int]):
        res=nums[0]
        l,r = 0,len(nums)-1
        while l<=r:
            # if we reach the subarray which is already sorted
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                break

            mid  = (l+r)//2
            res= min(res,nums[mid])
            if nums[mid]>= nums[l]:
                l=mid+1
            else:
                r=mid-1
        return res
    

if __name__=="__main__":
    sol=Solution()
    nums=[3,4,5,1,2]
    ans=sol.findMinimumInRotatedSortedArray(nums)
    print(ans)
