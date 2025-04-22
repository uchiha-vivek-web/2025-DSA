""" sum of primary and principal diagnal """

class Solution:
    def sumprincipaldiagnol(self,nums:list[list[int]])-> int :
        row:int = len(nums)
        col:int=len(nums[0])
        sum:int=0
        # condition for square matrix
        if row==col:
            for i in range(row):
                for j in range(col):
                    if i==j:
                        sum+=nums[i][j]
            return sum
    
    def sumsecondarydiagnol(self,nums:list[list[int]])-> int :
        row:int  = len(nums)
        col:int = len(nums[0])
        sum:int=0
        if row==col:
            for i in range(row):
                for j in range(col):
                    if( (i+j)==row-1):
                        sum+=nums[i][j]
            return sum

if __name__=="__main__":
    sol=Solution()
    nums=[[1,2],[3,4]]
    ans=sol.sumprincipaldiagnol(nums)
    ans1=sol.sumsecondarydiagnol(nums)
    print(ans1)