n=int(input())
k=int(input())
l=sorted([int(input()) for i in range(n)])
print(min([abs(l[i+k-1]-l[i]) for i in range(n-k+1)]))

# ip:
# 7
# 3
# 10
# 100
# 300
# 200
# 1000
# 20
# 30
# op:
# 20

# ip2:
# 10
# 4
# 1
# 2
# 3
# 4
# 10
# 20
# 30
# 40
# 100
# 200
# op2:
# 3