class Solution(object):
    def removeDuplicates(self, nums):
        # If the list is empty, no unique elements
        if not nums:
            return 0

        i = 0  # index of last unique element

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
# ---- Test code (for local run) ----
nums = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()
k = sol.removeDuplicates(nums)

print("k =", k)
print("Unique elements:", nums[:k])
