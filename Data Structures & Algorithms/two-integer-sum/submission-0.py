class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}
        for idx, val in enumerate(nums):
            res = target - val
            if res in values:
                return [values[res], idx]
            values[val] = idx
