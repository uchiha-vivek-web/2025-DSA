# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution :
    def containsDuplicate2(self,nums:list[int],k:int):
        window = set()
        L=0
        for R in range(len(nums)):
            if R-L > k :
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

sol= Solution()
nums=[1,2,3,1]
k=3
ans = sol.containsDuplicate2(nums,k)
print(ans)
