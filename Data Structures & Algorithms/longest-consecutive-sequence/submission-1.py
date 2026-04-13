class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictConsecutive = {}
        listIncrement = []
        maxLen = 1
        if not nums:
            return 0
        for idx in range(len(nums)):
            if nums[idx]-1 not in nums:
                dictConsecutive[nums[idx]] = nums[idx]+1
            else:
                listIncrement.append(nums[idx])
        for num in dictConsecutive.keys():
            curr = num
            currLen = 1
            while curr+1 in listIncrement:
                currLen+=1
                curr+=1
            if currLen > maxLen:
                maxLen = currLen
        return maxLen

        