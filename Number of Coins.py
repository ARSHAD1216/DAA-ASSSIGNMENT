def minCoins(coins, V):
    # Create a DP array to store the minimum number of coins for each value
    dp = [float('inf')] * (V + 1)
    
    # Base case: No coins are needed to make 0 value
    dp[0] = 0

    # Compute minimum coins required for all values from 1 to V
    for coin in coins:
        for i in range(coin, V + 1):
            if dp[i - coin] != float('inf'):  # If the subproblem has a solution
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[V] is still inf, it means it's not possible to make the value V
    return dp[V] if dp[V] != float('inf') else -1

# Driver code to test the function
coins = [1, 2, 5]  # List of available coins
V = 11  # Value to make

# Function call
result = minCoins(coins, V)
print(f"Minimum number of coins required: {result}")
