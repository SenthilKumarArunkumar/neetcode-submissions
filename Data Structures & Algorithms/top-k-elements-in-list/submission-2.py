class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      dic={}
      for num in nums:
        dic[num]=1+dic.get(num,0)
      l1=[]
      for num,cnt in dic.items():
        l1.append([cnt,num])
      l1.sort()
      l2=[]
      while(len(l2)<k):
        l2.append(l1.pop()[1])
      return l2