class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}

        for i in nums:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        
        for i in dic:
            if dic[i]>=2:
                return i
        return 0