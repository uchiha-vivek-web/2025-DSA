"""Find Non repeating character in a string"""
class Solution :
    def NonRepeatingCharacter(self,character:str):
        hash_map = {}
        for char in character :
            if char in hash_map :
                hash_map[char]+=1
            else :
                hash_map[char]=1
        for char in character :
            if hash_map[char] ==1 :
                return char
        return None

sol = Solution()
char = "vivek"
ans = sol.NonRepeatingCharacter(char)
print(ans)