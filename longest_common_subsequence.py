def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill dp array in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # dp[m][n] contains the length of the longest common subsequence
    return dp[m][n]

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
result = longest_common_subsequence(X, Y)
print("Length of Longest Common Subsequence:", result)
