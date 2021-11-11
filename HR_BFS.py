import queue as Qu
def BFS(s):
    q = Qu.Queue()
    q.put(s)
    visited[s] = True
    dist[s] = 0
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                dist[v] = dist[u] + 1


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    visited = [False]*n
    dist = [-1]*n

    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = int(input()) - 1

    BFS(s)
    for i in range(n):
        if i != s:
            print(dist[i]*6 if dist[i] != -1 else '-1', end = ' ')
    print()

# Input:
# 2
# 4 2
# 1 2
# 1 3
# 1
# 3 1
# 2 3
# 2

# Output:
# 6 6 -1
# -1 6

# Input2:
# 1
# 5 3
# 1 2
# 1 3
# 3 4
# 1

# Output2:
# 6 6 12 -1
