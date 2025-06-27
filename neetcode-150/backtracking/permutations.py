
# nums = [1,2,3]
# time complexity :O(n × n!)
# space complexity : O(n)


def permutation(nums:list[int]):
    result=[]
    used= [False]*len(nums)

    def backtrack(path):
        if len(path)== len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue

            used[i]=True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i]=False
    backtrack([])
    return result


print(permutation([1,2,3]))