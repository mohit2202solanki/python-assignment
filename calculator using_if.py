#Calculator
ch='y'
while ch=='y' or ch=='Y':
          i=input("Enter whether you want to perform operations on integer or float vlaues.\nPress I for int or F for float: ")
         
          if i=='i' or i=='I' or i=='f' or i=='F':
               n=int(input("Enter operation to perform:\n 1.Addition.\n 2.Subtraction.\n 3.Multiplication.\n 4.Division.\nEnter your choice: "))
               if n<=0 or n>4:
                  print("Invalid input")
               else:
                  if i=='i' or i=='I':    
                      a=int(input("\nEnter 1st number: "))
                      b=int(input("\nEnter 2nd number: "))

                      if n==1:
                         print("Addition= ",a+b)
                      elif n==2:
                         print("Subtraction= ",a-b)
                      elif n==3:
                         print("Multiplication= ",a*b)
                      elif n==4 :
                         if(b==0):
                            print("\nCan't divide a number by zero")
                         else:    
                            print("Division= ",a/b)
                      else:
                            default: print("Invalid input")
                  else:
                      a=float(input("\nEnter 1st number: "))
                      b=float(input("\nEnter 2nd number: "))
                      if n==1:
                         print("Addition= ",a+b)
                      elif n==2:
                         print("Subtraction= ",a-b)
                      elif n==3:
                         print("Multiplication= ",a*b)
                      elif n==4 :
                         if(b==0):
                            print("\nCan't divide a number by zero")
                         else:    
                            print("Division= ",a/b)
                      else:
                        default: print("Invalid input")
          else:
               print("Nothing to perform here")
          ch=input("\nEnter 'Y' to perform another operation: ")
        
