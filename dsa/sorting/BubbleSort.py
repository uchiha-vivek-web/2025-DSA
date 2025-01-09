class Sorting :
    def BubbleSort(self,nums:list[int]) :
        flag = False
        for i in range(1,len(nums)):
            flag = False
            for j in range(len(nums)-i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    flag=True

            if not flag :
                break
       

nums = [5,4,3,2,1]
sort = Sorting()
sort.BubbleSort(nums)
print(nums) 