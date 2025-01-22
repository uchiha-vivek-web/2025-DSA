class Solution : 
    def MissingInRange(self,nums:list[int],n:int,low:int,high:int):
        hash_set = set(nums)
        for x in range(low,high+1):
            if x not in hash_set:
                print(x,end=' ')

sol = Solution()
nums=[10,14,15]
n=len(nums)
low,high = 10,15
ans = sol.MissingInRange(nums,n,low,high)
print(ans)