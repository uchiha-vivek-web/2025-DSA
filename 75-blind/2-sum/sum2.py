
class Solution:
    def twosum(self,nums:list[int],target:int)-> list[int]:
        # nums = [2,1,5,3]
        map:dict={} # val:index
        for i,num in enumerate(nums):
            diff = target-num
            if diff in map:
                return [map[diff],i]
            map[num]=i
        return [-1,-1]
    
if __name__=="__main__":
    sol=Solution()
    nums = [2,1,5,3]
    target=4
    ans=sol.twosum(nums,target)
    print(ans)