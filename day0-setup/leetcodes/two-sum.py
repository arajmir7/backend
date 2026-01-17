class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # dictionary to store number : index

        for i in range(len(nums)):
            current = nums[i]
            needed = target - current

            if needed in seen:
                return [seen[needed], i]

            seen[current] = i

print(Solution().twoSum([2,7,11,15], 9))
