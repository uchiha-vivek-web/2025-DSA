""" Implementing sliding window """
""" Time complexity : O(N) """
""" Space complexity : O(1)  """
""" Reference : https://medium.com/@rishu__2701/mastering-sliding-window-techniques-48f819194fd7 """
class Solution :
    def max_subarray_sum(self,nums:list[int],k:int):
        max_sum = float('-inf')
        window_sum = sum(nums[:k])
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            max_sum = max(max_sum,window_sum)
        return max_sum

sol=Solution()
nums=[2,1,5,1,3,2]
k=3 # window size
ans=sol.max_subarray_sum(nums,k)
print(ans)