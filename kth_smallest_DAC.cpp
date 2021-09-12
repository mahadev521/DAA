#include <stdio.h>
int part(int a[], int low, int high)
{
    int left = low, right = high, middle, temp;
    middle = a[low];
    while (left < right)
    {
        while (a[left] <= middle)
            left++;
        while (a[right] > middle)
            right--;
        if (left < right)
        {
            temp = a[left];
            a[left] = a[right];
            a[right] = temp;
        }
    }
    a[low] = a[right];
    a[right] = middle;
    return right;
}
int ksmall(int a[], int start, int end, int k)
{
    if (start < end)
    {
        int middle = part(a, start, end);
        if (middle == k - 1)
            return a[middle];
        else if (middle > k - 1)
            return ksmall(a, start, middle, k);
        else
            return ksmall(a, middle + 1, end, k);
    }
}

int main()
{
    int a[100], n, i, k;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    printf("Enter the k value: ");
    scanf("%d", &k);
    printf("Enter the elements: ");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("The %d smallest element is %d", k, ksmall(a, 0, n - 1, k));
    return 0;
}
