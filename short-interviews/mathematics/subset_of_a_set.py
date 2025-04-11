""" find subset of an array/list """

# Neetcode Solution : https://www.youtube.com/watch?v=REOH22Xwdkk
""" Time complexity : O(N*2^N) """
""" Concept: Backtracking  """
class Solution :
    def subset(self,nums:list[int]):
        res=[]
        subset=[]

        def dfs(i):
            if i>= len(nums):
                res.append(subset.copy())
                return
            
            # descision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # descision to not include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
    
sol=Solution()
nums=[1,2,3]
ans=sol.subset(nums)
print(ans)