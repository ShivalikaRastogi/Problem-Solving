class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        coun=Counter(nums)
        a=[]
        n=len(nums)
        for key,value in coun.items():
            if value>(n//3):
                a.append(key)
        return a       
        
        