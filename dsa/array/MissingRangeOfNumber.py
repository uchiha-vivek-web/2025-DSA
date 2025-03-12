# https://www.geeksforgeeks.org/missing-ranges-of-numbers/
class Solution:
    def MissingRangeNumber(self,nums:list[int],lower:int,upper:int)->list:
        n=len(nums)
        res=[]
        # lower half
        if lower < nums[0]:
            res.append([lower,nums[0]-1])
        # mid section
        for i in range(n-1):
            if nums[i+1]-nums[i] > 1:
                res.append([nums[i+1],nums[i+1]-1])
        # upper half
        if upper > nums[-1]:
            res.append([nums[-1]+1,upper])
        return res
        
sol=Solution()
nums=[14,15,20,30,31,45]
start,end=10,50
ans=sol.MissingRangeNumber(nums,start,end)
print(ans)