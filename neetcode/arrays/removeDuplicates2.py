# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution:
    def removeDuplicates(self,nums:list[int]):
        l,r=0,0
        while r<len(nums):
            count=1
            while r+1<len(nums) and nums[r]==nums[r+1]:
                r+=1
                count+=1
            
            for i in range(min(2,count)):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l
    
if __name__=="__main__":
    nums= [0,0,1,1,1,1,2,3,3]
    sol=Solution()
    ans = sol.removeDuplicates(nums)
    print(ans)