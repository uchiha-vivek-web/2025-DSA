

class Solution:
    def two_pointer(self,nums:list[int],target:int)->bool:
        """space complexity : O(1) for sorting in place
            Time complexity : O(NlogN) --> sortng takes NlogN time
        """
        start,end = 0,len(nums)-1
        while start<end:
            current_sum = nums[start]+nums[end]
            if current_sum==target:
                return True
            elif current_sum> target:
                end-=1
            else :
                start+=1
        return False
    

sol = Solution()
nums=[1,2,3,5,7,9]
target=8
ans = sol.two_pointer(nums,target)
print(ans)           