class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        first_char = needle[0]
        found_index_start = []
        for i in range(len(haystack)):
            if first_char == haystack[i]:
                found_index_start.append(i)
        
        # Check if the next chars match the word
        for i in found_index_start:
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1