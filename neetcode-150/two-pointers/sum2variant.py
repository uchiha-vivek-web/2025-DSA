# two sum  variant 2

def two_sum(nums:list[int],target:int):
    # nums =[1,2,3,4]
    start,end=0,len(nums)-1
    while start<=end:
        if nums[start]+nums[end]==target:
            return [start,end]

        elif nums[start]+nums[end]<target:
            start+=1
        else:
            end-=1
    return -1



if __name__=="__main__":
    nums=[1,2,3,4]
    target=3
    ans=two_sum(nums,target)
    print(ans)