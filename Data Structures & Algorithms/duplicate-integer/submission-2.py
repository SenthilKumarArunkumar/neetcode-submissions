class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        flag=False
        for i,j in enumerate(nums):
            if j in dic:
                flag=True
                break
            else:
                dic[j]=i
        return flag
        
            