"""Bitonic array"""

class Solution:
    def BitonicArray(self,nums:list[int]):
        max=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>max:
                max=nums[i]
            else:
                break
        return max
    def BitonicArrayWithBinarySearch(self,nums:list[int]):
        n=len(nums)
        if n==1 or nums[0]>nums[1]:
            return nums[0]
        if nums[n-1]>nums[n-2]:
            return nums[n-1]
        start,end=1,n-2
        while start<=end:
            mid = (start+end)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return nums[mid]
            if nums[mid]<nums[mid+1]:
                start=mid+1
            else:
                end=mid-1
        return nums[end]

sol=Solution()
nums=[1,2,4,5,7,8,3]
ans=sol.BitonicArray(nums)
ans1 =sol.BitonicArrayWithBinarySearch(nums)
print(ans1)