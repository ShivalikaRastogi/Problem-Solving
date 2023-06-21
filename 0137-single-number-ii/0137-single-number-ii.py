class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            if nums.count(i)==1:
                 n += i  
        return n