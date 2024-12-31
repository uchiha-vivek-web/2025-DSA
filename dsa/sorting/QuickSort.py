
class Solution :
    def QuickSort(self,nums:list[int]):
        if len(nums) <=1 :
            return nums
        else :
            pivot = nums[0]
            less = [x for x in nums[1:] if x <= pivot]
            great = [x for x in nums[1:] if x> pivot]
            return self.QuickSort(less)+ [pivot] + self.QuickSort(great)
        
sol = Solution()
nums=[5,4,3,2,1]
ans = sol.QuickSort(nums)
print(ans)