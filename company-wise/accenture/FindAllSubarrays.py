""" Find all subarrays in an array """
class Soloution:
    def AllSubarrays(self,nums:list[int]) -> list :
        n:int=len(nums)
        result=[]
        for start in range(n):
            # if i begin from index 0 , in next loop i need to start from index1
            for end in range(start,n):
                result.append(nums[start:end+1])
        return result
    
    """ Find count of subarrays ."""
    def countOfSubarrays(self,nums:list[int]):
        n:int = len(nums)
        count=0
        for start in range(n):
            for _ in range(start,n):
                count+=1
        return count

if __name__=="__main__":
    sol=Soloution()
    nums=[1,2,3]
    ans=sol.AllSubarrays(nums)
    ans1=sol.countOfSubarrays(nums)
    print(ans1)



# direct formula for calculatig number of subarrays : N*(N+1)/2