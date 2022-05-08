a=int(input("Enter a year: "))

if a%4!=0 and a%100==0:
    print("Its  a leap year")
elif a%400==0:
    print("Its a leap year")
else:
    print("It is not leap year")
