def Kruskal(V,mat):
    mstsum=0
    mat=sorted(mat,key=lambda x:x[2])
    while (len(mat)>0):
        if mat[0][0] not in V[mat[0][1]-1] or mat[0][1] not in V[mat[0][0]-1]:
            V[mat[0][0]-1]=V[mat[0][0]-1] | V[mat[0][1]-1]
            V[mat[0][1]-1]=V[mat[0][0]-1]
            for i in V[mat[0][0]-1]: V[i-1]=V[mat[0][0]-1]
            mstsum+=mat[0][2]
        mat.pop(0)
    print(mstsum)

N,M=map(int,input().split())
mat,V=[],[]
[mat.append(list(map(int,input().split()))) for _ in range(M)]
[V.append(set([i])) for i in range(1,N+1)]
Kruskal(V,mat)

# Input:
# 4 6
# 1 2 5
# 1 3 3
# 4 1 6
# 2 4 7
# 3 2 4
# 3 4 5
# Output:
# 12

# Input:
# 5 7
# 1 2 20
# 1 3 50
# 1 4 70
# 1 5 90
# 2 3 30
# 3 4 40
# 4 5 60
# Output:
# 150
