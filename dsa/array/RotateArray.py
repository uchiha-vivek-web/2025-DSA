class Solution :
    def rotate(self,nums:list[int],k:int) -> None :
        n=len(nums)
        k=k%n
        # nums = [1,2,3,4,5]
        self.reverse(nums,0,n-1) # [5,4,3,2,1]
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
    # custom reverse function
    def reverse(self,nums:list[int],start:int,end:int) -> None :
        while start < end :
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1  

sol = Solution()
nums=[1,2,3,4,5]
k=2
sol.rotate(nums,k)
print(nums)