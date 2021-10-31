import sys
class Graph():

    def Display(self, dist):
        print("\nvertex \tsource distance")
        [print(f'{i}\t{dist[i]}') for i in range(self.v)]

    def minDistance(self, dist, sptSet):
        min = float('inf')
        for i in range(self.v):
            if dist[i] < min and sptSet[i] == False:
                min = dist[i]
                mindex = i
        return mindex

    def dijkstra(self, src):
        dist = [float('inf')] * self.v
        dist[src] = 0
        sptSet = [False] * self.v
        for _ in range(self.v):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.v):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.Display(dist)

g= Graph()
v=int(input('enter number of vertices: '))
g.v=v
g.graph=[([eval(x) for x in input().split()]) for i in range(v)]
g.dijkstra(int(input('give source: ')))

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
# enter number of vertices: give source: 
# vertex 	source distance
# 0	        19
# 1	        15
# 2	        7
# 3	        0
# 4	        9
# 5	        11
# 6	        13
# 7	        14
# 8	        9

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
# enter number of vertices: give source: 
# vertex 	source distance
# 0	        0
# 1	        4
# 2	        12
# 3	        19
# 4	        21
# 5	        11
# 6	        9
# 7	        8
# 8	        14