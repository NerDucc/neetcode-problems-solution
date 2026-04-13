class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        lenStr = len(s)
        maxLen = 0
        strLastSeen = {}
        for right, c in enumerate(s):
            if c not in strLastSeen or left > strLastSeen[c]:
                strLastSeen[c] = right
                maxLen = max(maxLen, right-left+1)
            else:
                left = strLastSeen[c]+1
                strLastSeen[c] = right
        return maxLen