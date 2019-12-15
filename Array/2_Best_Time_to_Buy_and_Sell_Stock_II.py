# -*- coding:utf-8 -*-

# Topic: Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: list) -> int:
        # @param prices, a list of integer
        # @return an integer
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit

    print(maxProfit.__annotations__)

if __name__ == '__main__':

    res = Solution().maxProfit([7,1,5,3,6,4])

    print(res)
