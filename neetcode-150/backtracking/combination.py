


def combination(nums:list[int],k:int):
    result=[]

    def backtrack(start,path):
        if len(path)==k:
            result.append(path[:])
            return

        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()

    backtrack(0,[])
    return result

print(combination([1,2,3],1))