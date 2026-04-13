class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_counter = Counter(s1)
        left = 0
        for right in range(len(s2)):
            if right - left + 1 == len(s1):
                if s1_counter == Counter(s2[left:right+1]):
                    return True
                else:
                    left+=1
        return False