""" 2 sum part 2 """
""" nums=[1,3,4,5,7,10,11]"""

class Solution:
    """ Time : O(N)
        Space : O(1)  """
    def twoSum2(self,nums:list[int],target:int):
        start,end=0,len(nums)-1
        while start<end :
            if nums[start] + nums[end] > target :
                end-=1
            elif nums[start] + nums[end] < target :
                start+=1
            else :
                return [start,end]
        return []
    
    def twoSum2Brute(self,nums:list[int],target:int):
        pass

sol=Solution()
nums=[1,3,4,5,7,10,11]
target=9
ans=sol.twoSum2(nums,target)
print(ans)