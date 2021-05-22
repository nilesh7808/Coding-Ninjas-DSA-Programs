def TowerOfHanoi(n,source,aux,dest):
    if n == 1:
        print(source,dest)
        return
    TowerOfHanoi(n-1,source,dest,aux)
    print(source,dest)
    TowerOfHanoi(n-1,aux,source,dest)

n = int(input())
TowerOfHanoi(n,'a','b','c')
