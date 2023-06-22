class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        arry = [i[-1] + i[:-1] for i in s]
        arry.sort()
        L = []
        for i in arry:
            L.append(i[1:])
            
        return ' '.join(L)