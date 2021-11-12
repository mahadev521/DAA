'''4. Find Shortest path from any node to any other node (All pairs shortest path)
within a graph.'''

def paths(path, v, u, route):
    if path[v][u] == v: return
    paths(path, v, path[v][u], route)
    route.append(path[v][u])

def display(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                paths(path, v, u, route)
                route.append(u)
                print(f'shortest path from {v} to {u}: ', *route)
 
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
    display(path, n)
 
ver = int(input('enter number of vertices of graph: '))
inf = float('inf')
G=[[eval(x) for x in input().split()] for i in range(ver)]
for i in range(ver):
    for j in range(ver):
        if G[i][j]==0 and i!=j: G[i][j]=inf
floyd(G,ver)

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
# shortest path from 0 to 1:  0 1
# shortest path from 0 to 2:  0 1 2
# shortest path from 0 to 3:  0 1 2 3
# shortest path from 0 to 4:  0 7 6 5 4
# shortest path from 0 to 5:  0 7 6 5
# shortest path from 0 to 6:  0 7 6
# shortest path from 0 to 7:  0 7
# shortest path from 0 to 8:  0 1 2 8
# shortest path from 1 to 0:  1 0
# shortest path from 1 to 2:  1 2
# shortest path from 1 to 3:  1 2 3
# shortest path from 1 to 4:  1 2 5 4
# shortest path from 1 to 5:  1 2 5
# shortest path from 1 to 6:  1 7 6
# shortest path from 1 to 7:  1 7
# shortest path from 1 to 8:  1 2 8
# shortest path from 2 to 0:  2 1 0
# shortest path from 2 to 1:  2 1
# shortest path from 2 to 3:  2 3
# shortest path from 2 to 4:  2 5 4
# shortest path from 2 to 5:  2 5
# shortest path from 2 to 6:  2 5 6
# shortest path from 2 to 7:  2 5 6 7
# shortest path from 2 to 8:  2 8
# shortest path from 3 to 0:  3 2 1 0
# shortest path from 3 to 1:  3 2 1
# shortest path from 3 to 2:  3 2
# shortest path from 3 to 4:  3 4
# shortest path from 3 to 5:  3 2 5
# shortest path from 3 to 6:  3 2 5 6
# shortest path from 3 to 7:  3 2 5 6 7
# shortest path from 3 to 8:  3 2 8
# shortest path from 4 to 0:  4 5 6 7 0
# shortest path from 4 to 1:  4 5 2 1
# shortest path from 4 to 2:  4 5 2
# shortest path from 4 to 3:  4 3
# shortest path from 4 to 5:  4 5
# shortest path from 4 to 6:  4 5 6
# shortest path from 4 to 7:  4 5 6 7
# shortest path from 7 to 2:  7 6 5 2
# shortest path from 7 to 3:  7 6 5 2 3
# shortest path from 7 to 4:  7 6 5 4
# shortest path from 7 to 5:  7 6 5
# shortest path from 7 to 6:  7 6
# shortest path from 7 to 8:  7 8
# shortest path from 8 to 0:  8 2 1 0
# shortest path from 8 to 1:  8 2 1
# shortest path from 8 to 2:  8 2
# shortest path from 8 to 3:  8 2 3
# shortest path from 8 to 4:  8 2 5 4
# shortest path from 8 to 5:  8 2 5
# shortest path from 8 to 6:  8 6
# shortest path from 8 to 7:  8 7
