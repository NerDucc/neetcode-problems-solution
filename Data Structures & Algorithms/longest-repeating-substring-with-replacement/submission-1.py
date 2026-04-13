class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        count = {}
        left = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            maxLen = max(count[s[right]], maxLen)
            if (right - left + 1) - maxLen > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
