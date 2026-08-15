class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i,j in  enumerate(nums):
            if j in dic:
                return True
            else:
                dic[j]=i
        return False