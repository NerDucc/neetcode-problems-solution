class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        print(numsSet)
        maxLen = 1
        if not nums:
            return 0
        for num in numsSet:
            if num-1 not in numsSet:
                curr = num
                currLen = 1
                while curr+1 in numsSet:
                    currLen+=1
                    curr+=1
                if currLen > maxLen:
                    maxLen = currLen
        return maxLen  


        