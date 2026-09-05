class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minbuy=prices[0]
        for sells in prices:
            maxp=max(maxp,sells-minbuy)
            minbuy=min(minbuy,sells)
        return maxp