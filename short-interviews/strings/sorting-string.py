""" Sorting string """

class Solution :
    def sortString(self,s:str):
        return sorted(s)

sol=Solution()
s="vivek"
ans=sol.sortString(s)
print(ans)