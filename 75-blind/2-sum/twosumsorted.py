"""2 sum in sorted array"""


class Solution:
    def mapsum(self,nums:list[int],target:int)-> list[int]:
        map={} # O(N)
        for i , num in enumerate(nums): # value : index
            difference = target-num
            if difference in map:
                return [map[difference],i]
            map[num]=i
        return [-1,-1]
    # 2 pointer techniques
    def twopointer(self,nums:list[int],target:int)->list[int]:
        left:int=0
        right:int=len(nums)-1
        while left<=right:
            sum:int = nums[left]+nums[right]
            if sum < target :
                left+=1
            elif sum > target:
                right-=1
            else:
                return [left,right]
        return [-1,-1]
    

if __name__=="__main__":
    sol=Solution()
    nums:list=[1,2,3,5]
    target:int=8
    ans:list[int] = sol.mapsum(nums,target)
    ans1:list[int]=sol.mapsum(nums,target)
    print(ans1)