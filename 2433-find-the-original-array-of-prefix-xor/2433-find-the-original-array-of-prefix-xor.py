class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prefix=[pref[0]]
        for i in range(1,len(pref)):
            prefix.append(pref[i-1]^pref[i])
        return prefix