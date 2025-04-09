""" Reverse a string """

class Solution:
    def ReverseString(self, s: str) -> str:
        return s[::-1]  # Correctly reverse the input string
    
    def scrathReverseString(self,s:str):
        """ converting list t string takes time compexity of O(N)"""
        """ .join returns new string of Space complexity of O(N)"""
        current_str = [ char for char in s ]
        i=0
        j=len(s)-1
        while i < j :
            temp=current_str[i]
            current_str[i]=current_str[j]
            current_str[j]=temp
            j-=1
            i+=1
        return "".join(current_str)




sol = Solution()
s = 'vivek'
ans = sol.ReverseString(s)
print(ans)

"""
Complexity Analysis :
Time Complexity : O(N) 
Space Complexity : O(N) -> a new string is createdd that is exact copy of the original string .
 
"""