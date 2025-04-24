

class Solution:
    def combine(self,n:int,k:int)-> list[list[int]]:
        res=[]
        def backtrack(start,comb):
            if len(comb)==k:
                res.append(comb.copy())
                return
            for i in range(start,n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
        backtrack(1,[])
        return res
        

if __name__=="__main__":
    n:int=4
    k:int=2
    sol=Solution()
    ans=sol.combine(n,k)
    print(ans)