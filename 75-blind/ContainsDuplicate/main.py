

class Solution:
    # O(n*n) -> TC
    def containsDuplicateBruteForce(self,nums:list[int])->bool:
        # arr = [1,2,3,1]
        n = len(nums)
        for i in range(n):
            for j in range(1,n):
                if nums[i]==nums[j]:
                    return True
        return False
    
    def containsDuplicateSort(self,nums:list[int]):
        # TC : O(nlogn)
        nums.sort()
        #  [1,1,2,3]
        n = len(nums)
        for i in range(n):
            if nums[i]==nums[i+1]:
                return True
        return False
    
    def containsDuplicate(self,nums:list[int]):
        # TC : o(n) , SC: O(N)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3,1]
    ans:bool=sol.containsDuplicateBruteForce(nums)
    ans1:bool=sol.containsDuplicateSort(nums)
    ans2:bool = sol.containsDuplicate(nums)
    print(ans2)