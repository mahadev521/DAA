#include<stdio.h>
void sort(int pro[],int wt[],int n)
{
	int i,j,temp;
	float ratio[n];
	for(i=0;i<n;i++)
	  ratio[i]=((float)(pro[i]))/(wt[i]);
	for(i=0;i<n-1;i++)
	 for(j=0;j<n-1-i;j++)
	  if(ratio[j]<ratio[j+1])
	  {
	  	temp=pro[j];
	  	pro[j]=pro[j+1];
	  	pro[j+1]=temp;
	  	temp=wt[j];
	  	wt[j]=wt[j+1];
	  	wt[j+1]=temp;
	  }
}
int knapsack(float Weight,int pro[],int wt[],int n)
{
	float u=Weight;
	int op=0,i;
	for(i=0;i<n;i++)
	{
		if(wt[i]>u)
		  break;
		else
		{
			op=op+pro[i];
			u=u-wt[i];
		}
	}
	if(i<n)
	 op=op+((u/wt[i])*pro[i]);
	return op;
}
int main()
{
	int n,i;
	printf("Enter the number of items: ");
	scanf("%d",&n);
	int pro[n],wt[n];
	float Weight;
	printf("Enter the value of knapsack: ");
	scanf("%f",&Weight);
	for(i=0;i<n;i++)
	{
		printf("Enter the weight and profit of item %d: ",i);
		scanf("%d%d",&wt[i],&pro[i]);
	}
	sort(pro,wt,n);
	printf("\nThe optimal profit is %d",knapsack(Weight,pro,wt,n));
}