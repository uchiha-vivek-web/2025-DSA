""" Reverse a string """

class Solution:
    def ReverseString(self, s: str) -> str:
        return s[::-1]  # Correctly reverse the input string

sol = Solution()
s = 'vivek'
ans = sol.ReverseString(s)
print(ans)

"""
Complexity Analysis :
Time Complexity : O(N) 
Space Complexity : O(N) -> a new string is createdd that is exact copy of the original string .
 
"""