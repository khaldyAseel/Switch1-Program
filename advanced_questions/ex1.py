# construction 

def min_cost(num_houses, cost):
   
    if num_houses == 0 or not cost or len(cost) != num_houses:
        return 0
    
    # Initialize DP array
    dp = [[0] * 3 for _ in range(num_houses)]
    
    # Base case: cost for the first house
    dp[0] = cost[0]
    
    # Fill the DP array
    for i in range(1, num_houses):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    # Minimum cost for the last house
    return min(dp[-1])


size = 3
list = [[3,5,10],
        [2,4,8],
        [6,9,13]]
print(f"min cost to bulid {size} houses is:{min_cost(size,list)}")