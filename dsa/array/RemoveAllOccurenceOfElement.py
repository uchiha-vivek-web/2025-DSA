class Solution :
    def RemoveOccurence(self,nums:list[int],ele:int)-> int :
        counter = 0
        for i in range(len(nums)):
            if nums[i] != ele :
                nums[counter] = nums[i]
                counter+=1
        return counter
    
nums= [3,2,2,3]
ele=2
sol = Solution()
ans= sol.RemoveOccurence(nums,ele)
print(ans)