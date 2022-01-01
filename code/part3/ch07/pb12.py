class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit_max = max(profit_max, price - min_price)
        
        return profit_max