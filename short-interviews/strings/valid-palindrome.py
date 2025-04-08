""" Valid Pallindrome """

class Solution :
    def isValidPallindrome(self,s:str)-> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr+=c.lower()
        
        return newStr == newStr[::-1]


sol = Solution()
s="abccbd"
ans = sol.isValidPallindrome(s)
print(ans)