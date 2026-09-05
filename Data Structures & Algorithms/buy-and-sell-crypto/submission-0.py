class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        ms=0
        while(l<r and l<len(prices) and r<len(prices)):
            s=prices[r]-prices[l]
            ms=max(s,ms)
            if(r==len(prices)-1):
                l+=1
                r=l+1
            else:
                r+=1
        return ms