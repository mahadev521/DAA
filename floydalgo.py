'''4. Find Shortest path from any node to any other node (All pairs shortest path)
within a graph.'''

def paths(path, v, u, route):
    if path[v][u] == v: return
    paths(path, v, path[v][u], route)
    route.append(path[v][u])

def display(path, n, cost):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                paths(path, v, u, route)
                route.append(u)
                print(f'with distance: {cost[v][u]}\tshortest path from {v} to {u} is ',*route)
 
def floyd(G,n):
    if not G: return
    cost = G.copy()
    path = [[None for x in range(n)] for y in range(n)]
    for v in range(n):
        for u in range(n):
            if v == u: path[v][u] = 0
            elif cost[v][u] != float('inf'): path[v][u] = v
            else: path[v][u] = -1
    for k in range(n):
        for v in range(n):
            for u in range(n):
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]
    display(path, n, cost)
 
ver = int(input('enter number of vertices of graph: '))
inf = float('inf')
G=[[eval(x) for x in input().split()] for i in range(ver)]
for i in range(ver):
    for j in range(ver):
        if G[i][j]==0 and i!=j: G[i][j]=inf
floyd(G,ver)

# # ip:
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
# with distance: 4        shortest path from 0 to 1 is  0 1
# with distance: 12       shortest path from 0 to 2 is  0 1 2
# with distance: 19       shortest path from 0 to 3 is  0 1 2 3
# with distance: 21       shortest path from 0 to 4 is  0 7 6 5 4
# with distance: 11       shortest path from 0 to 5 is  0 7 6 5
# with distance: 9        shortest path from 0 to 6 is  0 7 6
# with distance: 8        shortest path from 0 to 7 is  0 7
# with distance: 14       shortest path from 0 to 8 is  0 1 2 8
# with distance: 4        shortest path from 1 to 0 is  1 0
# with distance: 8        shortest path from 1 to 2 is  1 2
# with distance: 15       shortest path from 1 to 3 is  1 2 3
# with distance: 22       shortest path from 1 to 4 is  1 2 5 4
# with distance: 12       shortest path from 1 to 5 is  1 2 5
# with distance: 12       shortest path from 1 to 6 is  1 7 6
# with distance: 11       shortest path from 1 to 7 is  1 7
# with distance: 10       shortest path from 1 to 8 is  1 2 8
# with distance: 12       shortest path from 2 to 0 is  2 1 0
# with distance: 8        shortest path from 2 to 1 is  2 1
# with distance: 7        shortest path from 2 to 3 is  2 3
# with distance: 14       shortest path from 2 to 4 is  2 5 4
# with distance: 4        shortest path from 2 to 5 is  2 5
# with distance: 6        shortest path from 2 to 6 is  2 5 6
# with distance: 7        shortest path from 2 to 7 is  2 5 6 7
# with distance: 2        shortest path from 2 to 8 is  2 8
# with distance: 19       shortest path from 3 to 0 is  3 2 1 0
# with distance: 15       shortest path from 3 to 1 is  3 2 1
# with distance: 7        shortest path from 3 to 2 is  3 2
# with distance: 9        shortest path from 3 to 4 is  3 4
# with distance: 11       shortest path from 3 to 5 is  3 2 5
# with distance: 13       shortest path from 3 to 6 is  3 2 5 6
# with distance: 14       shortest path from 3 to 7 is  3 2 5 6 7
# with distance: 9        shortest path from 3 to 8 is  3 2 8
# with distance: 21       shortest path from 4 to 0 is  4 5 6 7 0
# with distance: 22       shortest path from 4 to 1 is  4 5 2 1
# with distance: 14       shortest path from 4 to 2 is  4 5 2
# with distance: 9        shortest path from 4 to 3 is  4 3
# with distance: 10       shortest path from 4 to 5 is  4 5
# with distance: 12       shortest path from 4 to 6 is  4 5 6
# with distance: 13       shortest path from 4 to 7 is  4 5 6 7
# with distance: 16       shortest path from 4 to 8 is  4 5 2 8
# with distance: 11       shortest path from 5 to 0 is  5 6 7 0
# with distance: 12       shortest path from 5 to 1 is  5 2 1
# with distance: 4        shortest path from 5 to 2 is  5 2
# with distance: 11       shortest path from 5 to 3 is  5 2 3
# with distance: 10       shortest path from 5 to 4 is  5 4
# with distance: 2        shortest path from 5 to 6 is  5 6
# with distance: 3        shortest path from 5 to 7 is  5 6 7
# with distance: 6        shortest path from 5 to 8 is  5 2 8
# with distance: 9        shortest path from 6 to 0 is  6 7 0
# with distance: 12       shortest path from 6 to 1 is  6 7 1
# with distance: 6        shortest path from 6 to 2 is  6 5 2
# with distance: 13       shortest path from 6 to 3 is  6 5 2 3
# with distance: 12       shortest path from 6 to 4 is  6 5 4
# with distance: 2        shortest path from 6 to 5 is  6 5
# with distance: 1        shortest path from 6 to 7 is  6 7
# with distance: 6        shortest path from 6 to 8 is  6 8
# with distance: 8        shortest path from 7 to 0 is  7 0
# with distance: 11       shortest path from 7 to 1 is  7 1
# with distance: 7        shortest path from 7 to 2 is  7 6 5 2
# with distance: 14       shortest path from 7 to 3 is  7 6 5 2 3
# with distance: 13       shortest path from 7 to 4 is  7 6 5 4
# with distance: 3        shortest path from 7 to 5 is  7 6 5
# with distance: 1        shortest path from 7 to 6 is  7 6
# with distance: 7        shortest path from 7 to 8 is  7 8
# with distance: 14       shortest path from 8 to 0 is  8 2 1 0
# with distance: 10       shortest path from 8 to 1 is  8 2 1
# with distance: 2        shortest path from 8 to 2 is  8 2
# with distance: 9        shortest path from 8 to 3 is  8 2 3
# with distance: 16       shortest path from 8 to 4 is  8 2 5 4
# with distance: 6        shortest path from 8 to 5 is  8 2 5
# with distance: 6        shortest path from 8 to 6 is  8 6
# with distance: 7        shortest path from 8 to 7 is  8 7
