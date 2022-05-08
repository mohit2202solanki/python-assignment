n=int(input("Enter total items: "))
r=int(input("Enter number of items to arrange: "))

fact_n=1;
#claculate n factorial      
for i in range (1,n+1):
      fact_n*=i
#Calculate n-r factorial
x=n-r
fact_x=1      
for i in range(1,x+1):
      fact_x*=i;
p=fact_n/fact_x;
print("P=",p)      
      
      
