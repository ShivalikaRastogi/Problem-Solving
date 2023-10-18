class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        pre = defaultdict(list)
        for a,b in relations:
            pre[b].append(a)
        @cache
        def dfs(n):
            if not pre[n]:
                return time[n-1]
            res = 0
            for i in pre[n]:
                res = max(res,time[n-1] + dfs(i))
            return res 
        out = 0
        for i in range(1,n+1):
            out = max(out,dfs(i))
        return out