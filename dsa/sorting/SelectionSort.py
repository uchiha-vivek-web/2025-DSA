class Solution :
    def SelectionSort(self,nums:list[int]):
        n=len(nums)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if nums[j] < nums[min_index]:
                    min_index=j
            nums[i],nums[min_index] = nums[min_index],nums[i]

nums = [5,4,3,2,1]
sol = Solution()
sol.SelectionSort(nums)
print(nums)