"""Find greatest common divisor by Euclid's algorithm"""

class Solution:
    def EuclidAlgorithm(self, a, b):
        if b == 0:
            return a
        else:
            return self.EuclidAlgorithm(b, a % b)

sol = Solution()
ans = sol.EuclidAlgorithm(4, 2)
print(ans)
