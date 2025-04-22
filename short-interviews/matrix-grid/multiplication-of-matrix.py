"""multiplication of two matrices"""

class Solution:
    def multiplymatrix(self,nums1:list[list[int]],nums2:list[list[int]]):
        r1,c1 = len(nums1), len(nums1[0])
        r2,c2 = len(nums2) , len(nums2[0])
        if c1 != r2 :
            print('matrix multiplication not possible')
        final_dim = r1*c2
        res = [[0] * c2 for _ in range(r1)]

        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    res[i][j] += nums1[i][k] * nums2[k][j]
        return res
    

if __name__=="__main__":
    sol=Solution()
    nums1=[[1,1],[2,2]]
    nums2=[[1,1],[2,2]]
    ans=sol.multiplymatrix(nums1,nums2)
    print(ans)

        