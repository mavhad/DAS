#Write a program to reverse an array or string
def reverselist(A,start,end):
    if start >= end:
        return
    A[start],A[end]=A[end],A[start]
    reverselist(A, start+1, end-1)

A = [1,2,3,4,5,6]
print(A)
reverselist(A, 0, 5)   
print(A)    
