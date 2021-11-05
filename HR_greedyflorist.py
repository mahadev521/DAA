n,k=map(int,input().split())
l=sorted([eval(x) for x in input().split()],reverse=True)
cost=prepur=0
for i in range(n):
    cost += (prepur +1)*l[i]
    prepur += 1 if (i+1)%k==0 else 0
print(cost)

# ip:
# 3 3
# 2 5 6
# op:
# 13

# ip1:
# 3 2
# 2 5 6
# op1:
# 15

# ip2:
# 5 3
# 1 3 5 7 9
# op2:
# 29
