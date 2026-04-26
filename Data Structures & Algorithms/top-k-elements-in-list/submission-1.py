from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums) + 1)]
        
        counter = Counter(nums)

        for num, count in counter.items():
            buckets[count].append(num)
        
        results = []

        for i in range(len(nums), 0, -1):
            for item in buckets[i]:
                results.append(item)
                if len(results) == k:
                    return results



        