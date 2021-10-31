def part(a, first, last):
    left, right, middle, temp = first, last, a[first], 0
    while left < right:
        while a[left] <= middle:
            left += 1
        while a[right] > middle:
            right -= 1
        if left < right:
            temp = a[left]
            a[left] = a[right]
            a[right] = temp
    a[first] = a[right]
    a[right] = middle
    return right

def small(a, start, end, k):
    if start < end:
        middle = part(a, start, end)
        if middle == k-1:
            return a[middle]
        elif middle > k-1:
            return small(a, start, middle, k)
        else:
            return small(a, middle+1, end, k)

x = int(input('enter number of elements: '))
y = [eval(x) for x in input('enter elements: ').split()]
k = int(input('enter k: '))
print(f'The {k} smallest element is {small(y,0,x-1,k)}')
