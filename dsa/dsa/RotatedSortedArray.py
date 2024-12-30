class Solution:
    def findMin(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]


# Test Cases
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_regular_case(self):
        nums = [3, 4, 5, 1, 2]
        self.assertEqual(self.sol.findMin(nums), 1)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.sol.findMin(nums), 1)

    def test_sorted_array(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.findMin(nums), 1)

    def test_with_duplicates(self):
        nums = [2, 2, 2, 0, 1]
        self.assertEqual(self.sol.findMin(nums), 0)

    def test_rotated_array(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.sol.findMin(nums), 0)

if __name__ == "__main__":
    unittest.main()
