
# nums = [1,2,3]
# time complexity : O(2^n)
# space complexity : o(n)
def subsets(nums:list[int]):
    result:list[int] = []

    def backtrack(start,path):
        result.append(path[:])

        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop() # undo the choice / backtrack
        
    backtrack(0,[])
    return result


print(subsets([1,2,3]))