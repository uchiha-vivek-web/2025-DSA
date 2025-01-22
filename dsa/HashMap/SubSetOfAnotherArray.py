class Solution :
    def  isSubset(self,nums1:list[int],nums2:list[int])-> bool : 
        hash_set = set(nums1)
        for num in nums2 :
            if num not in hash_set :
                return False
        return True
    def isSubsetForString(self,arr1:list[str],arr2:list[str])->bool:

        hash_set = set(arr1)
        for character in arr2 :
            if character not in hash_set:
                return False
        return True

        



sol = Solution()
nums1=[1,2,3,4,5]
nums2=[1,2,3]
arr1= ['a','b','c','d']
arr2=['a','f']
ans1 = sol.isSubset(nums1,nums2)
ans2= sol.isSubsetForString(arr1,arr2)
print(ans2)

