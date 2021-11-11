def minDistance( dist, sptSet):
    min = float('inf')
    for i in range(v):
        if dist[i] < min and sptSet[i] == False:
            min = dist[i]
            mindex = i
    return mindex

def dijkstra( src):
    dist = [float('inf')] * v
    dist[src] = 0
    sptSet = [False] * v
    for _ in range(v):
        x = minDistance(dist, sptSet)
        sptSet[x] = True
        for y in range(v):
            if graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
    [print(f'{src} -> {i}: {dist[i]}') for i in range(v)]

v=int(input('enter number of vertices: '))
graph=[[eval(x) for x in input().split()] for _ in range(v)]
dijkstra(int(input('give source: ')))

# imput:
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
# 3

# output:
# 3 -> 0: 19
# 3 -> 1: 15
# 3 -> 2: 7
# 3 -> 3: 0
# 3 -> 4: 9
# 3 -> 5: 11
# 3 -> 6: 13
# 3 -> 7: 14
# 3 -> 8: 9

# ----------------------------------------------------------------------------------------------------
# ip2:
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
# 0

# op2:
# 0 -> 0: 0
# 0 -> 1: 4
# 0 -> 2: 12
# 0 -> 3: 19
# 0 -> 4: 21
# 0 -> 5: 11
# 0 -> 6: 9
# 0 -> 7: 8
# 0 -> 8: 14
