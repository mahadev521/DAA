#this code donot use numpy and gives all possible solutions for n queens problem
def display(mat):
    for r in mat:
        print(*r)
    print()

def isSafe(mat, r, c):
    for i in range(r):
        if mat[i][c] == 1:
            return False
    i, j = r, c
    while i >= 0 and j >= 0:
        if mat[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    i, j = r, c
    while i >= 0 and j < len(mat):
        if mat[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    return True
 
 
def nQueen(mat, r):
    if r == len(mat):
        display(mat)
        return
    for i in range(len(mat)):
        if isSafe(mat, r, i):
            mat[r][i] = 1
            nQueen(mat, r + 1)
            mat[r][i] = 0
 
n = int(input('enter number of queens: '))
if n<4:
    print('there is no such arrangement')
else:
    mat = [[0 for x in range(n)] for y in range(n)]
    nQueen(mat, 0)
