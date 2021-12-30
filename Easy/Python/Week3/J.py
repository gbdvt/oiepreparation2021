a=int(input()) # 1 Piedra 2 Papel 3 Tijeras
b=int(input())
if a==1 and b==3:
    print("FIRST")
elif a==1 and b==2:
    print("SECOND")
elif a==2 and b==1:
    print("FIRST")
elif a==2 and b==3:
    print("SECOND")
elif a==3 and b==1:
    print("SECOND")
elif a==3 and b==2:
    print("FIRST")
else:
    print("DRAW")