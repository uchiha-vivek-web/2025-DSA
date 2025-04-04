""" Merging 2 sorted arrays """
""" Space complexity : O(N) """
""" Time complexity : O(N)   """
class Solution :
    def mergeSortedArray(self,nums1,nums2):
        i,j=0,0
        merged=[]

        while i < len(nums1) and j < len(nums2) :
            if nums1[i]<nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        
        while i < len(nums1):
            merged.append(nums1[i])
            i+=1
        while j < len(nums2):
            merged.append(nums2[j])
            j+=1
        return merged
    
sol=Solution()
nums1=[1,2,3]
nums2=[4,5]
result = sol.mergeSortedArray(nums1,nums2)
print(f'Merged Array is : {result} ')