arr = [13, 24, 54, 86, 12];     
temp = 0;    
        
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
       
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     
#Displaying elements of the array after sorting    
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
