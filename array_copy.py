arr1 = ['R', 'A', 'M', 'A', 'N'];     
     
arr2 = [None] * len(arr1);    
     
#Copying all elements of one array into another    
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i];     
     
#Displaying elements of array    
print("Elements of original array: ");    
for i in range(0, len(arr1)):    
   print(arr1[i]),    
     
print();    
          
print("Elements of new array: ");    
for i in range(0, len(arr2)):    
   print(arr2[i]),  
