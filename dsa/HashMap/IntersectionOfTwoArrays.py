"""Intersection of Two Arrays"""

class Solution :
    def intersection(self,nums1:list[int],nums2:list[int])->list:
        set1 = set(nums1)
        set2= set(nums2)
        res = []
        for num in set2 :
            if num in  set1 :
                res.append(num)
        return res

sol = Solution()
nums1=[1,2,3]
nums2=[3,2,6]
ans =sol.intersection(nums1,nums2)
print(ans)
