class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nonDupList = set()
        for num in nums:
            if num not in nonDupList:
                nonDupList.add(num)
            else:
                return True
        return False
            
        