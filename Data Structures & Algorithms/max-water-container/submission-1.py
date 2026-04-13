class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        curr = 0
        while i < j:
            if heights[i] < heights[j]:
                curr = max(curr, heights[i] * (j-i))
                i+=1
            else:
                curr = max(curr, heights[j] * (j-i))
                j-=1
        return curr