class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currDay = 0
        lowestPrice = prices[currDay]
        maxDay = len(prices)-1
        maxSell = 0
        currSell = 0
        while currDay <= maxDay:
            print(prices[currDay])
            if prices[currDay] <= lowestPrice:
                lowestPrice = prices[currDay]
                maxSell = max(currSell, maxSell)
                currSell = 0
            else:
                currSell = prices[currDay] - lowestPrice
                maxSell = max(currSell, maxSell)
            currDay+=1
        return maxSell
            
                
