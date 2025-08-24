def min_num_squares(n):
    squares = [i * i for i in range(1, int(n**0.5) + 1)]
   
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  
    
    for i in range(1, n + 1):
        for sq in squares:
            if sq > i:
                break
            dp[i] = min(dp[i], dp[i - sq] + 1)
    
    return dp[n]


n = int(input().strip())
print(min_num_squares(n))
