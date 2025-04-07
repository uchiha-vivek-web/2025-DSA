""" Simply rotate the array """

class Solution :
    def rotate(self,nums:list[int]):
        l,r = 0,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1
        return nums

sol=Solution()
nums=[1,2,3,4,5]
ans=sol.rotate(nums)
print(ans)