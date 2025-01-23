class Solution:
    def RemoveDuplicateElement(self, nums: list[int]) -> list[int]:
        hash_set = set()
        arr = []
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
                arr.append(num)
        return arr

sol = Solution()
nums = [2, 2, 3, 2]
ans = sol.RemoveDuplicateElement(nums)
print(ans)
