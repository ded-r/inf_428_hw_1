from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        arr_length = len(nums)
        result = curr_length = 1
    
        for i in range(1, arr_length):
            if nums[i - 1] < nums[i]:
                curr_length += 1
            else:
                curr_length = 1
            result = max(result, curr_length)
      
        return result