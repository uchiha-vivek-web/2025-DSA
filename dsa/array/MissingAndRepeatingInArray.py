"""Find missing and repeating number in an array"""
# class Solution :
#     def findMissingAndRepeating(self,nums:list[int]):
#         repeat=[]
#         for num in nums:
#             if num not in repeat:
#                 repeat.append(num)
#             else :
#                 return num
#         return -1
                

# sol=Solution()
# nums=[3,1,2]
# ans=sol.findMissingAndRepeating(nums)
# print(ans)

class Solution:
    def missingNumber(self,nums:list[int]):
        n=len(nums)
        for i in range(1,n+1):
            if i not in nums:
                return i
        return -1
    
sol=Solution()
nums=[3,1,3]
ans=sol.missingNumber(nums)
print(ans)