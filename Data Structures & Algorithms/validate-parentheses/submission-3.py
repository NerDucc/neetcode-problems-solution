class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {
            ')':'(', 
            '}':'{', 
            ']':'[',
        }
        stack = []
        if len(s)%2 != 0:
            return False
        else:
            for char in s:
                if char in valid_dict.values():
                    stack.append(char)
                elif char in valid_dict.keys():
                    if not stack:
                        return False
                    else:
                        if stack[-1] == valid_dict[char]:
                            stack.pop()
                        else:
                            return False
        return not stack
        