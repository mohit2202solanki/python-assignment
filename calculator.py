#Calculator

m=int(input("Enter operation to perform:\n 1.Addition.\n 2.Subtraction.\n 3.Multiplication.\n 4.Division\nEnter your choice: "))

def calcul(n):
    a=int(input("\nEnter 1st number: "))
    b=int(input("\nEnter 2nd number: "))
    
    switcher={
              1: a+b,     
              2: a-b,         
              3: a*b,           
              4: a/b                 
            }
    return switcher.get(n,"Invalid input")
if m==1 or m==2 or m==3 or m==4:
  print(calcul(m))
else:
    print("Invalid input")
