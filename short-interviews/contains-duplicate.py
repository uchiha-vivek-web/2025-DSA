""" whether an array contains duplicate or not """
# https://leetcode.com/problems/contains-duplicate/submissions/1598349790/
class Solution:
    def duplicateArray(self,nums:list[int]):
        """ using hashest TC:O(1) SC:O(N) """
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    
    def duplicateArrayBrute(self,nums:list[int]):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
    
    def duplicateArraySort(self,nums:list[int]):
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i]==nums[i+1]:
                return True
            
        return False


sol=Solution()
nums=[1,2,3,1]
nums1=[1,2,3]
ans=sol.duplicateArray(nums)
ans1 = sol.duplicateArrayBrute(nums)
ans2 = sol.duplicateArraySort(nums)
print(ans2)