class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        n = len(matrix)
        if n==0:
            return res
        m = len(matrix[0])
        
        dp = [[0 for k in range(m)] for l in range(n)]
                    
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    res = 1
                    
        for i in range(1,n):
            for j in range(1,m):
                if (dp[i][j] != 0):
                    dp[i][j] = min(min(dp[i-1][j-1],dp[i-1][j]),dp[i][j-1]) + 1
                    if res < dp[i][j]:
                        res = dp[i][j]
        return res*res
