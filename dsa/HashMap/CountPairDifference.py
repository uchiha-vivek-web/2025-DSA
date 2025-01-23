class Solution :
    @staticmethod
    def count_pairs(nums,k):
        n=len(nums)
        hash_map={}
        count=0
        for i in range(n):
            """Absolute  differece k ."""
            if (nums[i] + k) in hash_map : 
                count+= hash_map[nums[i]+k]
            if ( nums[i] -k) in hash_map :
                count+= hash_map[nums[i]-k]
            hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
        return count

sol = Solution()
nums = [8, 16, 12, 16, 4, 0]
k=4
ans =sol.count_pairs(nums,k)
print(ans)