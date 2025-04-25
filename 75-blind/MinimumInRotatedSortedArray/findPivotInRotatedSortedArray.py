


class Solution :
    def findPivot(self,nums:list[int]):
        # nums = [3,4,5,1,2]
        low=0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2

            if mid<high and nums[mid]> nums[mid+1]:
                return mid
            if low<mid and nums[mid]<nums[mid-1]:
                return mid-1
            
            if nums[low]<=nums[mid]: # left side is sorted
                low=mid+1
            else:
                high=mid-1
        return -1
    

if __name__=="__main__":
    sol=Solution()
    nums=[3,4,5,1,2]
    ans=sol.findPivot(nums)
    print(ans)