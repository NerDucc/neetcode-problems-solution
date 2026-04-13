class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        
        for idx, num in enumerate(nums):
            dictNums[num] = idx

        for idx, _ in enumerate(nums):
            findTarget = target - nums[idx]
            if findTarget in dictNums.keys() and idx != dictNums[findTarget]:
                return [idx, dictNums[findTarget]]

