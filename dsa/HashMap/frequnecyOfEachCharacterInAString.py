class Solution :
    def frequencyOfCharacter(self,character:str):
        freq_map = {}
        for char in character :
            if char in freq_map:
                freq_map[char]+=1
            else :
                freq_map[char]=1
        return freq_map
    
    """For list of nums"""
    def listOfNums(self,nums:list[int]):
        hash_map={}
        for num in nums :
            if num in hash_map :
                hash_map[num] +=1
            else :
                hash_map[num]=1
        return hash_map

sol = Solution()
chars = "viyek"
nums=[1,2,3,1]
ans = sol.frequencyOfCharacter(nums)
print(ans)