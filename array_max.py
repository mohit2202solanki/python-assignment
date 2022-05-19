arr = [55, 51, 8, 1, 90];     
         
max = arr[0];    
     
#Loop through the array    
for i in range(0, len(arr)):      
   if(arr[i] > max):    
       max = arr[i];    
           
print("Largest element present in given array: ", max);   
