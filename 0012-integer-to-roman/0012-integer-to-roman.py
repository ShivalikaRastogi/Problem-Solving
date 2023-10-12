class Solution:
    def intToRoman(self, data: int) -> str:
        A = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX'}
        roman = ''
        d = [int(i) for i in list(str(data).rjust(4, '0'))]
        while sum(d):
            while d[-1]:
                if d[-1] in A:
                    roman = A[d[-1]] + roman
                    d[-1] -= d[-1]
                else:
                    roman = A[1] + roman
                    d[-1] -= 1
            d = d[:-1]
            if len(d)==3:
                A = {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'}
            elif len(d)==2:
                A = {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'}
            elif len(d)==1:
                A = {1: 'M'}
        return roman