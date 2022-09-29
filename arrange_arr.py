def arrange(a):
    N = []
    P = []
    for i in range(len(a)):
        if a[i]<0:
            N.append(a[i])
        else:
            P.append(a[i])
    N = N.sort()
    P = P.sort()
    arr = N + P            

a = [-1,-2,0,3,2]
arrange(a)
print(arr)