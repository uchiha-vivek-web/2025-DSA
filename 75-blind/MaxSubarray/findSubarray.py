

class Solution:
    def findMaxSubarray(self,nums:list[int]):
        n:int = len(nums)
        result=[]
        for start in range(n):
            for end in range(start+1,n+1):
                result.append(nums[start:end])
        return result
    

if __name__=="__main__":
    sol=Solution()
    nums:list[int]=[1,2,3]
    ans=sol.findMaxSubarray(nums)
    print(ans)