
# PROBLEM LINK : https://leetcode.com/problems/find-the-middle-index-in-array/description/
class Solution :
    def findMiddleIndex(self,nums:list[int]):
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            if  left_sum==right_sum-nums[i]:
                return i
            left_sum+=nums[i]
            right_sum-=nums[i]
        return -1
    


if __name__=='__main__':
    sol=Solution()
    nums=[2,3,-1,8,4]
    ans=sol.findMiddleIndex(nums)
    print(ans)