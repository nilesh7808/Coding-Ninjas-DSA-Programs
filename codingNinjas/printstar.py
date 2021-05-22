N = int(input())
for i in range(1,N):
    for j in range(1,N):
        if j <= 5 - i:
            print("*",end = " " )
        else:
            print(" ",end=" ")
    print()
