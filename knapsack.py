'''6. Calculate the optimal profit of a Knapsack using Branch and Bound Technique. '''
n=int(input('enter number of items: '))
val1=[-1*eval(x) for x in input('enter values/profits of items: ').split()]
wt1=[eval(x) for x in input('enter weights of items: ').split()]
ex=sorted(list(zip(val1,wt1)),key=lambda x:x[1])
val,wt=zip(*ex)
W=int(input('enter knapsack capacity: '))
knap=[1]*n
w=lb=0
for j in range(n):
    if w+wt[j]<=W:
        w+=wt[j]
        lb+=val[j]
upper=lb
lb+=((val[j]/wt[j])*(W-w))
for i in range(n):
    lb1=up1=0
    w1=0
    for j in range(n):
        if i!=j and w1+wt[j]<=W and knap[j]==1:
                w1+=wt[j]
                lb1+=val[j]
    up1=lb1
    lb1+=((val[j]/wt[j])*(W-w1))
    if upper>lb1: 
        if upper>up1:
            knap[i]=0
            upper=up1
        elif lb1<lb:
            knap[i]=0
            lb=lb1
        elif lb1==lb:
            if upper>up1:
                knap[i]=0
                upper=up1
                lb=lb1
print(f'optimal profit {-1*upper}')
print('objects included: ')
for i in range(n):
    if knap[i]==1:
        print(f'object with profit {-1*val[i]} and weight {wt[i]}')

# ip:
# 4
# 10 10 12 18
# 2 4 6 9
# op:
# 38

# ip2:
# 3
# 60 100 120
# 10 20 30
# 50
# op2:
# 220

# ip3:
# 4
# 10 6 5 1
# 9 6 7 3
# 16
# op3:
# 16
