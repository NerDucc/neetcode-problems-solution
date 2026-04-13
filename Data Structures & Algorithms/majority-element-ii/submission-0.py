class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n_3_times = len(nums)//3
        majorityDict = {}
        for num in nums:
            majorityDict[num] = 1 + majorityDict.get(num, 0)
        res = []
        for key in majorityDict.keys():
            if majorityDict[key] > n_3_times:
                res.append(key)
        return res