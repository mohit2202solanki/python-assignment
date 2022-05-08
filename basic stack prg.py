s1='22+12-15/4'
s2=''
stack=[]

for i in range(0,len(s1)):
   if (s1[i].isnumeric()):
         s2+=s1[i]
   elif s1[i]=='+' or s1[i]=='-' or s1[i]=='*' or s1[i]=='/':
        s2+=(s1[i])
   else:
       print('no operation')
while stack:
    s2+=stack.pop()

print(s2," ")    
''' elif s1[i]=='+' or s1[i]=='-' or s1[i]=='*' or s1[i]=='/'
        stack.append(s1[i])
    elif s1[i]=='(':
        stack.append(s1[i])
    elif s1[i]==')':
        while stack[-1]!='(':
            s2+=stack.pop()
    else:
        print('no operation')'''
