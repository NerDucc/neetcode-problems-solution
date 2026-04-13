class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupChar = {}
        for s in strs:
            lst = []
            dictChar = {chr(i): 1 for i in range(ord('a'), ord('z')+1)}
            for char in s:
                dictChar[char] +=1
            strDict = str(dictChar)
            lst = groupChar.get(strDict) or []
            lst.append(s)
            groupChar[strDict] = lst
        result = []
        for val in groupChar.values():
            result.append(val)
        return result

        
            
        
