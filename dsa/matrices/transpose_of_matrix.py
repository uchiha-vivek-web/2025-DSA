from typing import List

class Solution:
    def transposeOfMatrix(self, nums: List[List[int]]) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])

        # Create a new matrix with swapped dimensions
        transpose = [[0] * row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                transpose[j][i] = nums[i][j]

        return transpose

sol = Solution()
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = sol.transposeOfMatrix(nums)
print(ans)
