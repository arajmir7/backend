class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            # If opening bracket, push to stack
            if ch in mapping.values():
                stack.append(ch)
            else:
                # Closing bracket with no matching open
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()

        # Valid only if no unmatched brackets remain
        return len(stack) == 0
