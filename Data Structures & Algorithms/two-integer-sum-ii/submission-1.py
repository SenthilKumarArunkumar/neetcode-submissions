class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        for i,e in enumerate(numbers):
            diff=target-e
            if diff in dic:
                return [(dic[diff]+1),(i+1)]
            else:
                dic[e]=i