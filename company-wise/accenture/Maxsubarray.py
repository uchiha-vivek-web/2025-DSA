# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def MaxSubarray(self,nums:list[int]):
        res:int = nums[0]
        total:int=0
        for num in nums:
            if total<0:
                total=0
            total+=num
            res = max(res,total)
        return res

if __name__=="__main__":
    sol=Solution()
    nums=[5,4,-1,7,8]
    ans=sol.MaxSubarray(nums)
    print(ans)