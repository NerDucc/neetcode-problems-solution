from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = defaultdict(int)
        result = []
        for num in nums:
            freqDict[num]+=1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in freqDict.items():
            buckets[count].append(num)
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result