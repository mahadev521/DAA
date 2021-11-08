def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l, r = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(l, r, arr.copy())


def merge(l, r, merged):
    left, right = 0, 0
    while left < len(l) and right < len(r):
        if l[left] <= r[right]:
            merged[left+right]=l[left]
            left += 1
        else:
            merged[left + right] = r[right]
            right += 1
    for left in range(left, len(l)):
        merged[left + right] = l[left]
    for right in range(right, len(r)):
        merged[left + right] = r[right]
    return merged

n=int(input('enter number of elements: '))
l=[eval(x) for x in input('enter elements: ').split()]
l=merge_sort(l)
k=int(input('enter k: '))
print(f'{k} smallest element is {l[k-1]}')
