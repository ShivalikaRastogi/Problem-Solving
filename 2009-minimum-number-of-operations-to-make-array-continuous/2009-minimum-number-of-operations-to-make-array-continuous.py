class Solution(object):
    def minOperations(self, A):
        n = len(A)
        ans = n
        hash_set = set()
    
        for x in A:
            hash_set.add(x)
    
        unique = list(hash_set)
        unique.sort()
    
        j = 0
        m = len(unique)
    
        for i in range(m):
            while j < m and unique[j] < unique[i] + n:
                j += 1
            ans = min(ans, n - j + i)
    
        return ans        