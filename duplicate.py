def dupl(arr):  
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i]==arr[j]:
                return 1
            
    return 0

                  

arr = [1,2,3,4]
dupl(arr) 
print(bool(dupl(arr)))                 