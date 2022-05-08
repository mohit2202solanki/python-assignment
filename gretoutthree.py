# Greatest out of three numbers

n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
n3=int(input("Enter 3rd number: "))

if n1==n2==n3:
    print("All three values are equal")
elif n1==n2 and n2>n3:
    print(n1,"and",n2,"is greater than ",n3)
elif n2==n3 and n2>n1:
    print(n2,"and",n3," is greater than",n1)
elif n1==n3 and n3>n2:
    print(n1,"and",n3," is greater than ",n2)
elif n1>n2:
    if n1>n3:
        print(n1," is greatest")
    else:
        print(n3," is greatest")
else:
    print(n2," is greatest")
