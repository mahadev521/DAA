'''1. Find the min-max of list of elements using divide and conquer strategy.'''

def maxmin(a, x, y):
    maxi, mini = 0, 0
    d = e = f = [0, 0]
    if y-x <= 1:
        f[0] = max(a[int(x)], a[int(y)])
        f[1] = min(a[int(x)], a[int(y)])
    else:
        d = maxmin(a, x, (x + y)/2)
        e = maxmin(a, ((x + y)/2)+1, y)
        d[0] = max(d[0], e[0])
        d[1] = min(d[1], e[1])
    return d

x = int(input('enter number of elements: '))
y = [eval(x) for x in input('enter elements ').split()]
o = maxmin(y, 0, len(y)-1)
print('The maximum and minimum elements in given elements are: ', *o)
