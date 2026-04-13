class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for idx in range(len(nums)):
            pre = nums[idx+1:]
            suf = nums[0:idx]
            group = pre+suf
            total = 1
            for num in group:
                total *= num
            res.append(total)
        return res
        