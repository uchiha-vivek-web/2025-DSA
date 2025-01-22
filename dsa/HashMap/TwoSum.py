class Solution :
    def TwoSum(self,nums:list[int],target:int):
        hash_set=set(nums)
        for num in nums :
            compliment = target-num
            if compliment in hash_set :
                return True
            else :
                return False
    def TwoSumList(self,nums:list[int],target:int):
        hash_map = {}
        n=len(nums)
        for i in range(n):
            compliment = target- nums[i]
            if compliment in hash_map:
                return [hash_map[compliment],i]
            hash_map[nums[i]]=i
        return []



sol = Solution()
nums = [2,7,11,15]
target=9
ans =sol.TwoSumList(nums,target)
print(ans)
