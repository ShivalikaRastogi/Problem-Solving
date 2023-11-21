class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans,mp=0,{}
        for i in nums:
            rev=i-int((str(i)[::-1]))
            if rev not in mp:mp[rev]=1
            else:mp[rev]+=1
        print(mp)
        for i in mp:ans+=((mp[i]*(mp[i]-1)//2))%(10**9+7)
        return ans%(10**9+7)