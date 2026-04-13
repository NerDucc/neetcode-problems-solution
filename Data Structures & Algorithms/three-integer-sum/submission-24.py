class Solution:
   def threeSum(self, nums: List[int]) -> List[List[int]]:
       result = []
       numsSort = sorted(nums)
       for idx in range(len(numsSort) - 2):
           if idx > 0 and numsSort[idx] == numsSort[idx - 1]:
               continue
           lPoint = idx + 1
           rPoint = len(numsSort) - 1
           while lPoint < rPoint:
               total = numsSort[idx] + numsSort[lPoint] + numsSort[rPoint]
               if total == 0:
                   result.append([numsSort[idx], numsSort[lPoint], numsSort[rPoint]])
                   lPoint += 1
                   rPoint -= 1
                   while lPoint < rPoint and numsSort[lPoint] == numsSort[lPoint - 1]:
                       lPoint += 1
                   while lPoint < rPoint and numsSort[rPoint] == numsSort[rPoint + 1]:
                       rPoint -= 1
               elif total < 0:
                   lPoint += 1
               else:
                   rPoint -= 1
       return result