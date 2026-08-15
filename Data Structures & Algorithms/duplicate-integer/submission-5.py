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
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))      

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
"""