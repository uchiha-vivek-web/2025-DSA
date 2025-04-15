# PROBLEM LINK : https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

    def sumRange(self, prefix: list[int], L: int, R: int) -> int:
        if L == 0:
            return prefix[R]
        return prefix[R] - prefix[L - 1]

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    prefix_sum = sol.runningSum(nums)
    print("Prefix Sum:", prefix_sum)
    
    # Example: Find sum from index 1 to 3 (2 + 3 + 4 = 9)
    print("Sum from index 1 to 3:", sol.sumRange(prefix_sum, 1, 3))
