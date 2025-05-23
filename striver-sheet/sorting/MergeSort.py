class Solution:
    def MergeSort(self,nums:list[int]):
        n=len(nums)
        if len(nums)>1:
            mid=len(nums)//2
            left=nums[:1]
            right=nums[1:]
            self.MergeSort(left)
            self.MergeSort(right)
            i=j=k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    nums[k]=left[i]
                    i+=1
                else :
                    nums[k]=right[j]
                    j+=1
                k+=1
            while i < len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j < len(right):
                nums[k]=right[j]
                j+=1
                k+=1
            return nums
        
sol=Solution()
nums=[5,4,3,2,1]
ans=sol.MergeSort(nums)
print(ans)
