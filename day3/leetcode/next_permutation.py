class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2

        # 1️⃣ Find first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2️⃣ If found, swap with just larger element on the right
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3️⃣ Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])
