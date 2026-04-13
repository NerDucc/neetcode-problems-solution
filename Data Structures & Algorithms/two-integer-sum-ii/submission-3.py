class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lPoint = 0
        rPoint = -1
        while numbers[lPoint] + numbers[rPoint] != target:
            if numbers[lPoint] + numbers[rPoint] > target:
                rPoint-=1
            else:
                lPoint+=1
        return [lPoint+1, len(numbers)+rPoint+1]
        