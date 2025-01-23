"""Remove minimum elements such that no common elements exist in two arrays"""
class Solution : 
    def RemoveMinimumElement(self,nums1:list[int],nums2:list[int]):
        set1 = set(nums1)
        set2 =set(nums2)
        for num in nums1 :
            count=0
            if num  in set2 :
                count+=1
        return count
    
sol=Solution()
nums1=[1,2,3,4]
nums2=[2,3,4,5,8]
ans=sol.RemoveMinimumElement(nums1,nums2)
print(ans)