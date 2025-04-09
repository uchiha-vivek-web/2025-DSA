""" Split at those points where you get the digits """

import re

class Solution:
    def splitAtDigits(self,s:str):
        pattern='\d+'
        result=re.split(pattern,s)
        return result
    
sol = Solution()
s = 'hello 12 hi 89. Howdy 34'
ans=sol.splitAtDigits(s)
print(ans)