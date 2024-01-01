#User function Template for python3

class Solution:
    def hello(self,heights):
        stack=[]
        maxA=0
        for index,height in enumerate(heights):
            start=index
            while stack and stack[-1][1]>height:
                i,h=stack.pop()
                maxA=max(maxA,h*(index-i))
                start=i
            stack.append([start,height])

        for i,h in stack:
            maxA=max(maxA,h*(len(heights)-i))
        return maxA
   
    def maxArea(self,M, n, m):
        maxArea=0
        h = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if M[i][j]==1:
                    h[j]+=1
                else:
                    h[j]=0
            maxArea=max(maxArea,self.hello(h))
        return maxArea



#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends