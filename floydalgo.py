def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    for r in range(ver):
        for p in range(ver):
            for q in range(ver): dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    [print(*i) for i in dist]

ver = int(input('enter number of vertices: '))
inf = float('inf')
G=[[eval(x) for x in input().split()] for i in range(ver)]
for i in range(ver):
    for j in range(ver):
        if G[i][j]==0 and i!=j: G[i][j]=inf
floyd(G)

# ip:
# 9
# 0 4 0 0 0 0 0 8 0 
# 4 0 8 0 0 0 0 11 0 
# 0 8 0 7 0 4 0 0 2 
# 0 0 7 0 9 14 0 0 0 
# 0 0 0 9 0 10 0 0 0 
# 0 0 4 14 10 0 2 0 0 
# 0 0 0 0 0 2 0 1 6 
# 8 11 0 0 0 0 1 0 7
# 0 0 2 0 0 0 6 7 0

# op:
# enter number of vertices: 
# 0 4 12 19 21 11 9 8 14 
# 4 0 8 15 22 12 12 11 10 
# 12 8 0 7 14 4 6 7 2 
# 19 15 7 0 9 11 13 14 9 
# 21 22 14 9 0 10 12 13 16 
# 11 12 4 11 10 0 2 3 6 
# 9 12 6 13 12 2 0 1 6 
# 8 11 7 14 13 3 1 0 7 
# 14 10 2 9 16 6 6 7 0
