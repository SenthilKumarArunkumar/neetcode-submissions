class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorteds=set(nums)
        lon=0
        for num in sorteds:
            if(num-1 not in sorteds):
                lenn=1
                while((num+lenn) in sorteds):
                    lenn+=1
                lon=max(lon,lenn)
        return lon