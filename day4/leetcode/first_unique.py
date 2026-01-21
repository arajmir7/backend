class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        # Step 1: count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: find first character with frequency 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1
