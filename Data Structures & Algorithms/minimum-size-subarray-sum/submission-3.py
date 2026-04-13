class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        count = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                count = min(count, r - l + 1)
                total -= nums[l]
                l+= 1
                
        return count if count != float('inf') else 0

