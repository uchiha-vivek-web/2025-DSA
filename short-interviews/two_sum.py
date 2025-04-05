""" Two sum of an array """

""" Brute force approch """

class Solution :
    def twoSumBrute(self,nums:list[int],target:int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

    """ One pass hash table"""
    """ Time complexity O(N) """
    """ Space complexity O(N)  """
    def twoSum(self,nums,target):
        numMap={}
        for i,num in enumerate(nums):
            complement = target-num
            if complement in numMap:
                return [numMap[complement],i]
            numMap[num]=i


sol=Solution()
nums=[2,7,11,15]
target=9
ans = sol.twoSumBrute(nums,target)
print(ans)