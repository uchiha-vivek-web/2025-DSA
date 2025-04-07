""" Count of each element in list """

class Solution :
    def countElement(self,nums:list[int]):
        count_map={}
        for num in nums:
            if num in count_map:
                count_map[num]+=1
            else :
                count_map[num]=1
        return count_map
    

sol=Solution()
nums=[1,2,1,1,2,3,2]
ans=sol.countElement(nums)
print(ans)