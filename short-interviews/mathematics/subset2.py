

class Solution :
    def subset2(self,nums:list[int]):
        res=[]
        nums.sort()

        def backtrack(i,subset):
            if i == len(nums):
                res.append(subset[::])
                return
            

            # all subsets that includes nums[i]
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()

            while i + 1< len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1,subset)
        backtrack(0,[])
        return res
    

sol=Solution()
nums=[1,2,3]
ans=sol.subset2(nums)
print(ans)