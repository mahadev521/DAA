'''2. Find the kth smallest element using divide and conquer approach'''
def partition(a,l,h):
    pivot = a[l]
    i = l
    j=h
    while i<j:
        while a[i]<=pivot and i<h: i+=1
        while a[j]>pivot and j>l: j-=1
        if i<j: a[i],a[j]=a[j],a[i]   
    a[j],a[l]=a[l],a[j]
    return j

def quickSort(a,l,h):
    if l < h:
        pi = partition(a, l, h)
        quickSort(a, l, pi - 1)
        quickSort(a, pi + 1, h)
        

n=int(input('enter number of elements: '))
l=[eval(x) for x in input('enter elements: ').split()]
quickSort(l,0,n-1)
k=int(input('enter k: '))
print(f'{k} smallest element is {l[k-1]}')
