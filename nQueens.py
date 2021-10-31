import numpy as np
def display(l):
    # l=np.where(l>0,'\N{crown}','==')
    for i in l:
        print(*i)


def safe(l, row, col):
    for i in range(col):
        if l[row][i]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if l[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < n and j >= 0:
        if l[i][j]:
            return False
        i += 1
        j -= 1
    return True


def solve(l, col):
    if col >= n:
        return True
    for i in range(n):
        if safe(l, i, col):
            l[i][col] = 1
            if solve(l, col+1):
                return True
            l[i][col] = 0
    return False


n = int(input('enter number of queens: \n'))
l = np.zeros((n, n), dtype=int)
if n<4 or solve(l, 0) == False:
    print('No such arrangement')
else:
    display(l)

# ip:
# 8
# op:
# enter number of queens: 
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 1
# 0 1 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 1 0 0 0 0 0

# ip1: 
# 16
# op1:
# enter number of queens: 
# 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
# 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
# 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0