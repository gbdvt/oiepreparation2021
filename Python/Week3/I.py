l=[]
n=[]
for i in range(2):
    l+=[int(input())]
l.sort()
 
for i in range(2):
    n+=[int(input())]
n.sort()
 
if l[0]<=n[0] and l[1]<=n[1]:
    print("YES")
else:
    print("NO")