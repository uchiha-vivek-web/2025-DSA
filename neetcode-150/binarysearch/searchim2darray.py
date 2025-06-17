from typing import List
class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        # m=rows and n=cols
        ROWS,COLS= len(matrix),len(matrix[0])
        l,r  = 0, ROWS*COLS-1
        while l<=r:
            m  = l+ (r-l)//2
            row,col= m//COLS , m%COLS
            if target > matrix[row][col]:
                l=m+1
            elif target< matrix[row][col]:
                r=m-1
            else:
                return True
        return False
    

if __name__=="__main__":
    sol=Solution()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target=19
    
    ans=sol.searchMatrix1(matrix,target)
    print(ans)
