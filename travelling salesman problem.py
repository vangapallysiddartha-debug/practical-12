
INF = float('inf')

n = int(input("Enter number of cities: "))

print("Enter the cost matrix (use 999 for no direct path):")
cost = []

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

for i in range(n):
    for j in range(n):
        if cost[i][j] == 999:
            cost[i][j] = INF


dp = [[INF] * n for _ in range(1 << n)]

dp[1][0] = 0

for mask in range(1 << n):
    for u in range(n):
        if dp[mask][u] != INF:
            for v in range(n):
                if not (mask & (1 << v)) and cost[u][v] != INF:
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(
                        dp[new_mask][v],
                        dp[mask][u] + cost[u][v]
                    )

# Return to starting city
full_mask = (1 << n) - 1
answer = INF

for city in range(1, n):
    if cost[city][0] != INF:
        answer = min(
            answer,
            dp[full_mask][city] + cost[city][0]
        )

if answer == INF:
    print("No complete tour exists.")
else:
    print("Minimum travelling cost:", int(answer))
