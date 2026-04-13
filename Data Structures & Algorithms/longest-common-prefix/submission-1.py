class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prf, count = 0, 0
        valid_count = len(strs)
        strs_sort = sorted(strs, key=len)
        shortest_str = strs_sort[0]
        listS = ""
        for idx in range(len(shortest_str)):
            curC = shortest_str[idx]
            for s in strs_sort:
                if curC == s[idx]:
                    count+= 1
            if count == valid_count:
                prf += 1
            else:
                return shortest_str[0:prf]
            count = 0
        return shortest_str[0:prf]
            