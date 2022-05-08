a=int(input("Enter a number: "))

for i in range (2,a):
    if a%i==0:
         print("It is not a prime no.")
         break
    else:
       print("It is a prime no.")
       break
