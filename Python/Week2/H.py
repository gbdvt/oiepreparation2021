n=int(input())
x=int(input())
y=int(input())
if ((x==1 or x==n) and (y==1 or y==n)):
    print("2")
elif ((x==1 or x==n) or (y==1 or y==n)):
    print("3")
else:
    print("4")
    