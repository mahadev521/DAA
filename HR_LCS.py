n,m =list(map(int,input().split()))
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if x[i - 1] == y[j - 1]: dp[i][j] = 1 + dp[i - 1][j - 1]
        else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
i, j, v = n, m, []
while i > 0 and j > 0:
    if x[i - 1] == y[j - 1]:
        v.append(x[i - 1])
        i -= 1
        j -= 1
    else:
        if dp[i - 1][j] > dp[i][j - 1]: i -= 1
        else : j -= 1
print(*reversed(v))


# ip:
# 5 6
# 1 2 3 4 1
# 3 4 1 2 1 3
# op:
# 3 4 1 

# ip2:
# 9 10
# 3 9 8 3 9 7 9 7 0
# 3 3 9 9 9 1 7 2 0 6
# op2:
# 3 3 9 9 7 0
