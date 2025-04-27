

class Solution:
    def search(self,nums:list[int],target:int):
        # nums = [4,5,6,7,0,1,2]
        l,r=0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target==nums[mid]:
                return mid
            #left sorted portion
            if nums[l]<=nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            
            # right sorted portion
            else:
                if target<nums[mid] or target>nums[r]:
                    r=mid+1
                else:
                    l=mid+1


if __name__=="__main__":
    sol=Solution()
    nums=[4,5,6,7,0,1,2]
    target=1
    ans=sol.search(nums,target)
    print(ans)