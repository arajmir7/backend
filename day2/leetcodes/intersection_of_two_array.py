from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        result = []

        # Count frequency of nums1
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        # Check nums2 against the frequency map
        for num in nums2:
            if freq.get(num, 0) > 0:
                result.append(num)
                freq[num] -= 1

        return result
