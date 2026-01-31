class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left: int, right: int):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            # Odd length palindromes (center at i)
            expand(i, i)
            # Even length palindromes (center between i and i+1)
            expand(i, i + 1)

        return count
