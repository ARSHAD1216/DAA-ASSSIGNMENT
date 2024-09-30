def longest_common_subsequence(text1, text2):
    # Get the lengths of both strings
    m, n = len(text1), len(text2)

    # Create a 2D dp array with (m+1) x (n+1) dimensions initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:  # If characters match, extend the LCS
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Otherwise, take the max

    # The length of the LCS is in dp[m][n]
    return dp[m][n]

# Driver code to test the function
text1 = "abcde"
text2 = "ace"

# Function call
result = longest_common_subsequence(text1, text2)
print(f"Length of Longest Common Subsequence: {result}")
