class Solution:
    def findMin(self, nums: list[int]) -> int:
        start=0
        end = len(nums)-1
        while start < end :
            mid = (start+end)//2
            if nums[mid] <= nums[end]:
                end=mid
            else :
                start=mid+1
        return nums[start]
    

nums = [3,3,1,3]
sol = Solution()
ans = sol.findMin(nums)
print(ans)   