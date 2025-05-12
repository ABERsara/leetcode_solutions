# Last updated: 5/12/2025, 10:49:20 AM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price # update the minimum price so far
            elif price - min_price > profit:
                profit = price - min_price # update max profit
            
        return profit

        

        
            


