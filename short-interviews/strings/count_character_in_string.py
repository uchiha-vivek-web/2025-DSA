""" Count the number of characters in string """

class Solution :
    def CountCharacters(self,s:str):
        count={}
        for char in s:
            count[char] = count.get(char,0)+1
        return count


sol=Solution()
s="vivek"
ans=sol.CountCharacters(s)
print(ans)