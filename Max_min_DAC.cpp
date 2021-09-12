#include <stdio.h>
#define max(x, y) x > y ? x : y
#define min(x, y) x > y ? y : x
typedef struct pair
{
    int maxi;
    int mini;
} pair;
pair minmax(int a[], int x, int y)
{
    int maximum, minimum;
    pair t1, t2, t3;
    if (y - x <= 1)
    {
        t3.maxi = max(a[x], a[y]);
        t3.mini = min(a[x], a[y]);
    }
    else
    {
        t1 = minmax(a, x, (x + y) / 2);
        t2 = minmax(a, ((x + y) / 2) + 1, y);
        t3.maxi = max(t1.maxi, t2.maxi);
        t3.mini = min(t1.mini, t2.mini);
    }
    return t3;
}

int main()
{
    int a[100], n, i;
    pair t;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    printf("Enter the elements (space seperated): ");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    t = minmax(a, 0, n - 1);
    printf("Max= %d Min= %d", t.maxi, t.mini);
    return 0;
}
