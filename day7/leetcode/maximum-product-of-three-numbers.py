from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        # Case 1: product of three largest numbers
        case1 = nums[-1] * nums[-2] * nums[-3]
        
        # Case 2: product of two smallest and the largest
        case2 = nums[0] * nums[1] * nums[-1]
        
        return max(case1, case2)
