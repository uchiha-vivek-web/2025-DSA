

class Solution:
    def rob(self,nums:list[int])-> int :
        rob1,rob2=0,0
        for n in nums:
            temp =max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
    
    """ using recursion"""
    def robdfs(self,nums:list[int])-> int :
        def dfs(i):
            if i>= len(nums):
                return 0
            return max(nums[i] + dfs(i+2),dfs(i+1))
        return dfs(0)    


sol=Solution()
nums = [2,7,9,3,1]
ans=sol.rob(nums)
ans1=sol.robdfs(nums)
print(ans1)