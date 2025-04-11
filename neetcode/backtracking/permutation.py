
class Solution :
    def permutation(self,nums:list[int]):
        result = []

        # base case
        if len(nums)==1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permutation(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
    
sol=Solution()
nums=[1,2]
ans=sol.permutation(nums)
print(ans)