x,y=input(),list(input())
yl=len(y)
for i in x:
    if i in y: y.remove(i)
print((len(x)-yl)+(2*len(y)))
