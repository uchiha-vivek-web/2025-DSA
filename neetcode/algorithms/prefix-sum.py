


class Solution:
    def prefix_sum(self,nums:list[int]):
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1]=prefix[i]+nums[i]
        return prefix
    
    def range_sum(prefix,left,right):
        return prefix[right+1]-prefix[left]

sol = Solution()
nums=[1,2,3,4,5]
ans = sol.prefix_sum(nums)
print(ans)