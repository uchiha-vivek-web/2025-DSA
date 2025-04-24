


class Solution:
    def maxSubarray(self,nums:list[int])-> int :
        # nums=[-2,1,-3,4,-1]
        maxSub = nums[0]
        curSum=0
        for n in nums :
            if curSum<0:
                curSum=0
            curSum+=n
            maxSub = max(maxSub,curSum)
        return maxSub
    

if __name__=="__main__":
    sol=Solution()
    nums=[-2,1,-3,4,-1]
    nums1=[-2,1,-3,4,-1,2,1,-5,4]
    ans=sol.maxSubarray(nums1)
    print(ans)