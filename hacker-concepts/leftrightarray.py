def left_right_subarray(nums):
    n=len(nums)
    left = [0]*n
    right = [0]*n
    # left sub array
    for i in range(1,n):
        left[i] = left[i-1]+ nums[i-1]
    
    # right sub array
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] + nums[i+1]
    
    return left,right

def pivotIndex(nums:list[int]):
    pass

if __name__=="__main__":
    nums:list[int]=  [1,2,3,4]
    nums1:list[int] = [1,7,3,6,5,6]
    ans=left_right_subarray(nums1)
    print(ans)