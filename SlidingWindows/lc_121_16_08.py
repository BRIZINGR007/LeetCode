class Solution:
    def maxProfit(self, prices):
        left,right =0,1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(profit,maxP)
            else:
                left=right
            right+=1
            return maxP


            

z=Solution()
print(z.maxProfit(prices =[3,2,6,5,0,3]))

