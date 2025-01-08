class Solution :
    def ReverseAnArrayInPlace(self,nums:list[int],start:int,end:int) -> None :
        nums[start],nums[end] =  nums[end],nums[start]
        start+=1
        end-=1
    def ReverseAnArrayByExtraPlace(self,nums:list[int],start:int,end:int) :
        pass


sol = Solution()
nums=[1,2,3,4,5]
start,end=0,len(nums)-1
sol.ReverseAnArrayInPlace(nums,start,end)
print(nums)
        