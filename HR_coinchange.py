n,m=[eval(x) for x in input().split()]
c=[eval(x) for x in input().split()]
dp = [1]+[0]*n
for i in c:
    for j in range(i, n+1): dp[j] += dp[j-i]
print(dp[n])

# ip:
# 4 3
# 1 2 3
# op:
# 4

# ip2:
# 10 4
# 2 5 3 6
# op2:
# 5
