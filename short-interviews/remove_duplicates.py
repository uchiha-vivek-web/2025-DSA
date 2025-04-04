class Solution:
    def removingDuplicates(self,nums: list[int])-> int:
        k=0
        for i in range(1,len(nums)):
            if nums[k] != nums[i]:
                k+=1
                nums[k]=nums[i]
        
        return k+1

nums=[1,1,2,2]
solution=Solution()
new_length= solution.removingDuplicates(nums)
print(f' Length is : {new_length} ')
print(f' New array is : {nums[:new_length]}')

""" Space complexity : O(1) """
""" Time complexity : O(N)  """