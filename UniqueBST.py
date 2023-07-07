class Solution:
    def numTrees(self,N):
        # code here
        Ts = [0]*(N+1)
        Ts[0]=1
        for i in range(1,N+1):
            for j in range(i):
               Ts[i] = (Ts[i] + (Ts[j]*Ts[i-j-1]))%(10**9 + 7)
        return Ts[N]
