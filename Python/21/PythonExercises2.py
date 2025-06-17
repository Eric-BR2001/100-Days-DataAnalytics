def coin_change(coins, target_amount):
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0

    for amount in range(1, target_amount + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[target_amount] if dp[target_amount] != float('inf') else -1