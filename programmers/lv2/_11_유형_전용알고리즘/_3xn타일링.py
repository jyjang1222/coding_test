def solution(n):
    answer = 0
    mod = 1000000007
    dp = [0 for i in range(n + 1)]
    dp[1] = 2;
    dp[2] = 3;
    for i in range(3, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i - 1] % mod + dp[i-2] % mod
        else:
            dp[i] = dp[i - 1] * 2 % mod + dp[i - 2] % mod
        dp[i] = dp[i] % mod
    return dp[n]

n = 3
r =solution(n)
print(r)