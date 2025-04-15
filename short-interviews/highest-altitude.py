# https://leetcode.com/problems/find-the-highest-altitude/editorial/

class Solution :
    def highestAltitude(self,gain:list[int]):
        current_altitude=0
        highest_point=current_altitude
        for gains in gain:
            current_altitude+=gains
            highest_point =max(highest_point,current_altitude)
        return highest_point


if __name__=="__main__":
    sol=Solution()
    nums=[-5,1,5,0,-7]
    ans=sol.highestAltitude(nums)
    print(ans)
