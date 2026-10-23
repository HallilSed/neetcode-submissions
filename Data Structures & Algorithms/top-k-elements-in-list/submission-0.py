import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        

        res = set(nums)

        freq = {}

        tmp = list(res)
        for i in tmp:
            freq[i] = 0
        
        for i in nums:
            if i in res:
                freq[i] += 1
        
        return heapq.nlargest(k, freq, key=freq.get)
        