n=int(input())
m=int(input())
k=int(input())
total=n*m
change=1
for i in range(n+1):
    if k==m*i:
        print("YES")
        change=0
if change==1:
    for l in range(m+1):
        if k==n*l:
            print("YES")
            change=0
if change==1:
    print("NO")