# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        #Effective solution - pair every price with the lowest prior price. Keep best comparison. 

        for price in prices: 
            #Update buy price with lowest found price 
            if price < buy:
                buy = price 

            #Check if found profit is greater than old profit. Update if so. 
            tempProfit = price - buy
            if tempProfit > profit: 
                profit = tempProfit 

        return profit 