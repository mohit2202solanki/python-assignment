arr = [5, 4, 5, 3, 10, 7, 4, 3, 9];     
     
print("Duplicate elements in given array: ");    
   
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);    
