m = int(input("Enter num of rows: "))
n = int(input("Enter num of cols: "))
a = []
for i in range(m):
    b = []
    for j in range(n):
        j = int(input("Enter number in pocket ["+str(i)+"]["+str(j)+"]"))
        b.append(j)
    a.append((b))   
    print("Matrix is.....")
    for i in range(m):
        for j in range(n):
            print((a[i][j],end=" "))
        print()    
