class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0

        for n in range(0, len(prices)):
            for i in range(n+1, len(prices)):
                if prices[i] - prices[n] > a:
                    a = prices[i] - prices[n]

        return a