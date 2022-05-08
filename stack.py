#x = '35+18/4-3'
x=input("Enter an expression: ")
a = list(x)
print(a)
b = []
op1 = ''
for i in range(0, len(a)):
    op2 = ''
    if(ord(a[i]) >= 48 and ord(a[i]) <= 57):
        op1 += a[i]
    if(a[i] == '+' or a[i] == '-' or a[i] == '/' or a[i] == '' or a[i] == '*'):
        op2 += a[i]
        b.append(op1)
        op1 = ''
        b.append(op2)
    if(a[i] == a[len(a)-1]):
        b.append(op1)
print(b)
