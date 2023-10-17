class Solution:
    def longestPalindrome(self, s: str) -> int:
        singles = set()
        length = 0
        for i in s:
            if i in singles:
                singles.remove(i)
                length += 2
            else:
                singles.add(i)
        if len(singles): length += 1
        return length