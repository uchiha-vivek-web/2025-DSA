

""" Implementation of Kadan's algorithm ! """

class Solution:
    def KadanAlgorithmMax(self,nums:list[int]):
        currSum=maxSum = nums[0]
        for num in nums[1:]:
            currSum  = max(num,currSum+num)
            maxSum=max(maxSum,currSum)
        return maxSum
    
    def KadanAlgorithmMin(self, nums: list[int]) -> int:
        currSum = minSum = nums[0]
        for num in nums[1:]:
            currSum = min(num, currSum + num)  # ⬅️ Fix is here
            minSum = min(minSum, currSum)
        return minSum


if __name__=="__main__":
    sol=Solution()
    nums=[2,1,5,3]
    nums1= [3, -4, 2, -3, -1, 7, -5]
    nums2=[1,-2,0,-1]
    ans=sol.KadanAlgorithmMax(nums1)
    ans1=sol.KadanAlgorithmMin(nums2)
    print(ans1)