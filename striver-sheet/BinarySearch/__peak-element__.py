class Solution:
    """Time complexity : O(N)
        Space complexity : O(1)
    """
    def findPeakElement(self,nums:list[int]):
        n=len(nums)
        for i in range(n):
            if (i==0 or nums[i-1]<nums[i]) and (i==n-1 or nums[i]>nums[i+1]):
                return i
        return -1
    def findPeakElementBinarySearch(self,nums:list[int]):
        """Time complexity : O(LogN)
           Space complexity : O(1)
        """
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        low=1
        high=n-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]>nums[mid-1]:
                low=mid+1
            else:
                high=mid-1
        return -1
            



sol=Solution()
nums=[1,2,3,4,5,6,7,8,5,1]
ans=sol.findPeakElement(nums)
ans1=sol.findPeakElementBinarySearch(nums)
print(ans1)