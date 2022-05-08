x=int(input("Enter total items: "))
y=int(input("Enter number of items to arrange: "))

def fact(n):
    fact_n=1
    for i in range (1,n+1):
        fact_n*=i
    return(fact_n) 

fx=fact(x)
fy=fact(x-y)

p=fx/fy
print("P= ",p)
