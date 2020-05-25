class Solution:
    
    # think in terms of longest common subsequence matrix
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        lenA = len(A)
        lenB = len(B)
        dp = [[0]*(lenB + 1) for _ in range(lenA + 1)]
        
        for i in range(1, lenA+1):
            for j in range(1, lenB+1):
                dp[i][j] = 1 + dp[i-1][j-1] if A[i-1] == B[j-1] else max(dp[i-1][j], dp[i][j-1])
        
        return dp[lenA][lenB]