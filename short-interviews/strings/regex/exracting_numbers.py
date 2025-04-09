""" Extratacting numbers from the string. """

import re
class Solution :
    def extractNumbers(self,s:str):
        pattern = '\d+'
        result = re.findall(pattern,s)
        return result

sol=Solution()
s = 'hello 12 hi 89. Howdy 34'
ans=sol.extractNumbers(s)
print(ans)