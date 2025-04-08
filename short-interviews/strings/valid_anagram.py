""" Valid anagram """

class Solution :
    """ Time Complexity : O(s+t) -> O(N) """
    """ Space complexity : O(1)   """
    def valid_anagram(self,s:str,t:str):
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char,0) + 1

        for char in t :
            if char not in count:
                return False
            count[char] -=1
            if count[char] < 0:
                return False
            
        return True
    
    def valid_anagram_sorting(self,s:str,t:str):
        return sorted(s) == sorted(t)

sol=Solution()
s = "rat"
t="cat"
ans=sol.valid_anagram(s,t)
ans1 = sol.valid_anagram_sorting(s,t)
print(ans1)
