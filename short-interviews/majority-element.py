

class Solution :
    def findMajorityElement(self,nums:list[int]):
        """ Time complexity : O(N)
            Space complexity : O(N)
        """
        map={}
        max_count=len(nums)//2
        for num in nums:
            map[num] = map.get(num,0)+1
            if map[num] > max_count:
                return num
        return None
    



sol=Solution()
nums = [1,2,1,1,3,2,3]
ans= sol.findMajorityElement(nums)
print(ans)