class Solution :
    def InsertionSort(self,nums:list[int]):
        for i in range(1,len(nums)):
            temp = nums[i]
            j=i-1
            while j>=0 and temp<nums[j]:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=temp

nums =[5,4,3,2,1]
sol = Solution()
sol.InsertionSort(nums)
print(nums)