class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for idx in range(0,len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                prev_idx = stack.pop()
                ans[prev_idx] = idx-prev_idx
            stack.append(idx)
        return ans