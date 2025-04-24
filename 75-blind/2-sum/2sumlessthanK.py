# # Problem Statement:

# Given an array of integers nums and an integer k, find the maximum sum of any two distinct numbers in nums that is less than k.
# Return -1 if no such pair exists.
class Solution:
    def twosumlessthank(self,nums:list[int],target:int) :
        # nums = [34, 23, 1, 24, 75, 33, 54, 8]
        # Time complexity : O(NlogN)
        nums.sort()
        left:int=0
        right:int=len(nums)-1
        maxsum = 0
        while left < right :
            current_sum :int = nums[left]+nums[right]
            if current_sum > target :
                right-=1
            else:
                maxsum=max(current_sum,maxsum)
                left+=1
        return maxsum

    '''via brute force'''
    def twosumlessthankbf(self,nums:list[int],target:int):
        # nums = [34, 23, 1, 24, 75, 33, 54, 8]
        # Time complexity O(N^2)
        maxsum=-1
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                current_sum = nums[i] + nums[j]
                if current_sum < target:
                    maxsum = max(maxsum,current_sum)
        return maxsum

if __name__=="__main__":
    sol=Solution()
    nums = [34, 23, 1, 24, 75, 33, 54, 8]
    ans=sol.twosumlessthank(nums,60)
    ans1=sol.twosumlessthankbf(nums,60)
    print(ans1)