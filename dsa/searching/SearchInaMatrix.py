"""Search in a matrix"""

class Solution :
    def SearchInAMatrix(self,nums:list[list[int]],target:int)->bool:
        row=len(nums)
        col=len(nums[0])
        for i in range(row):
            for j in range(col):
                if nums[i][j]==target:
                    return True
        return False
    """Function to search the index"""
    def SearchIndex(self,nums:list[list[int]],target:int):
        row=len(nums)
        col=len(nums[0])
        for i in range(row):
            for j in range(col):
                if nums[i][j]==target:
                    return [i,j]
        return -1

    """Reducing search space"""
    def ReducingSearchSpace(self,nums:list[int],target:int):
        row=len(nums)
        col=len(nums[0])
        i=0
        j=col-1
        while i < row and j>= 0:
            if target > nums[i][j]:
                i+=1
            elif target<nums[i][j]:
                j-=1
            else :
                return True
        return False


sol=Solution()
nums=[[1,2,3],[4,5,6],[7,8,9]]
target=5
ans=sol.SearchInAMatrix(nums,target)
ans1=sol.SearchIndex(nums,target)
ans2=sol.ReducingSearchSpace(nums,target)
print(ans2)