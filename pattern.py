for i in range (1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("done")
"""*
**
***
****
*****"""
for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("done")
"""1
12
123
1234
12345"""
for i in range(1,6):
  for j in range(1,6):
       print("*",end=" ")
  print()
print("done")  
       
"""*****
*****
*****
*****
*****"""
for i in range(1,6):
    if (i==5):
      break
    print(i,end=" ")
    print()
    
"""1
2
3
4"""
for i in range(65,70):
  for j in range(65,i+1):
    print (chr(j),end=" ")
  print()
print("done")
"""A
AB
ABC
ABCD
ABCDE"""
print("1.addition")
print("2.subtraction")
print("3.divide")
print("4.multiplication")
n=int(input("enter the choice"))
a=int(input("enter the first number"))
b=int(input("enter the second number"))
if(n==1):
      s=a+b
      print("the addition of two number",s)
elif(n==2):
      s=a-b
      print("subtraction of two number",s)
elif(n==3):
      s=a/b
      print("divide of two number",s)
elif(n==4):
      s=a*b
      print("multiplication of two numbers",s)
else:
      print("wrong choice")
 
                  
      
