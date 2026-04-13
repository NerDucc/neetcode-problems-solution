class Solution:
    def isPalindrome(self, s: str) -> bool:
        sList = [alp.lower() for alp in s if alp.isalnum()]
        return sList == sList[::-1]
        