# constraint link : https://chatgpt.com/c/6856a812-1cdc-8008-87e7-b6f59013f2a0


from typing import List

class Solution:
    def maximumDifference(self,nums:List[int]):
        # [7,1,5,4]
        min_val=nums[0]
        max_diff=-1

        for i in range(1,len(nums)):
            if nums[i]>min_val:
                max_diff = max(max_diff,nums[i]-min_val)
            else:
                min_val=nums[i]
        return max_diff

    """some more constraints"""
    """ finding maximum difference in the array when j-i is even """
    def maximumDifferenceConstraint1(self,nums:List[int]):
        max_difference=-1
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (j-i) %2==0 and nums[j] - nums[i]:
                    max_difference = max(max_difference,nums[j]-nums[i])
        return max_difference
    

if __name__=="__main__":
    sol=Solution()
    nums:list[int] = [7,1,5,4]
    ans=sol.maximumDifference(nums)
    ans1 = sol.maximumDifferenceConstraint1(nums)
    print(ans1)