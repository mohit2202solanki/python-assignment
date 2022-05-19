arr = [8, 1, 7, 15, 6];        
    
min = arr[0];    
     
#Loop through the array    
for i in range(0, len(arr)):       
   if(arr[i] < min):    
       min = arr[i];    
     
print("Smallest element present in given array: ", min); 
