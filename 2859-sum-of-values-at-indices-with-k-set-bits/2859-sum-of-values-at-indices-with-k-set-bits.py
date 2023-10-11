class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        size = len(nums)
        sum = 0
        for i in range(0,size):
            value = bin(i)[2:]
            res = str(value).count('1')
            if res==k:
                sum = sum + nums[i]
        return sum;
                