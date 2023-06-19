class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        n = ''.join(digits)
        n = int(n)+1
        L = list(str(n))
        L = [int(i) for i in L]
        return L
