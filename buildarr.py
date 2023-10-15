class Solution:
    def __init__(self):
        self.count=0
        self.dp=[]
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.dp=[[[-1 for _ in range(m+1)] for __ in range(k+1)] for _ in range(n+1)]
        return self.numarr(n,m,k,-1)%((10**9)+7)
    
    def numarr(self,n,m,k,maxim):
        if(k>n):
            return 0
        if(n==0):
            if(k==0):
                return 1
            return 0
        if(self.dp[n][k][maxim]!=-1):
            return self.dp[n][k][maxim]
        if(k==0):
            self.dp[n][k][maxim]=maxim**n
            return maxim**n
        if(maxim==m):
            return 0
        result=0
        for i in range(1,m+1):
            if(i>maxim):
                result+=self.numarr(n-1,m,k-1,i)
            else:
                result+=self.numarr(n-1,m,k,maxim)
        self.dp[n][k][maxim]=result%((10**9)+7)
        return result%((10**9)+7)
