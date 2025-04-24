# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self,prices:list[int]):
        l,r=0,1
        maxProfit = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                l=r
            r+=1
        return maxProfit

if __name__=="__main__":
    sol=Solution()
    prices = [7,1,5,3,6,4]
    ans=sol.maxProfit(prices)
    print(ans)