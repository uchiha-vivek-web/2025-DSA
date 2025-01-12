class Solution : 
    def RemoveDuplicateFromSortedArray(self,nums:list[int])-> int :
        seen =set()
        idx=0
        for i in range(len(nums)):
            if nums[i] not in seen :
                seen.add(nums[i])
                nums[idx]=nums[i]
                idx+=1
        return idx
    

sol = Solution()
nums = [1,2,2,3,4,4,4,5,5]
ans = sol.RemoveDuplicateFromSortedArray(nums)
print(ans)
for i in range(ans):
    print(nums[i],end=' ')