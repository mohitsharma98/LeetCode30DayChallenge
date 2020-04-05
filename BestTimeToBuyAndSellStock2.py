"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).


Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==0):
            return 0
        profit = 0
        for i in range(0, len(prices)-1):
            if(prices[i+1] > prices[i]):
                profit += prices[i+1] - prices[i]
        return profit