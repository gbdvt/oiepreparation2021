a=0
b=0
for i in range(3):
    x=int(input())
    if x%2==0:
        a=1
    if x%2:
        b=1
print("YES" if a==1 and b==1 else "NO")