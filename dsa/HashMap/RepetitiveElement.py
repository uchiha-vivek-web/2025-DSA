class Solution :
    def RepetitiveElement(self,nums:list[int]):
        hash_map ={}
        for num in nums :
            if num in hash_map:
                hash_map[num] +=1
            else :
                hash_map[num]=0
        for num in nums :
            if hash_map[num]==1 :
                return num
        return None
    
sol = Solution()
nums = [1, 3, 2, 3, 4]
ans = sol.RepetitiveElement(nums)
print(ans)