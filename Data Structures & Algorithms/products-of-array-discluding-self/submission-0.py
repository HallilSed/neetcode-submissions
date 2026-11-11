class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = len(nums) * [0]
        prefix = 1

        i = 0
        while i < len(nums):

            answer[i] = prefix
            prefix *= nums[i]

            i += 1
        
        suffix = 1
        i = len(nums) - 1
        while i >= 0:

            answer[i] *= suffix
            suffix *= nums[i]

            i -= 1

        return answer