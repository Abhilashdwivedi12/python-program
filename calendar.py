"""a=int(input("enter the number"))
def fact(a):
    if(a==0)or (a==1):
      return 1
    else:
        return a*fact(a-1)
print(fact(a))
y=int(input("enter the number"))
calender.setfirstweekday(calendar,MONDAY)
c1=calendar.calendar(y)
print(c1)
import calendar
y=int(input("enter the number"))
c1=calendar.calendar(y)
print(c1)
mm=int(input("enter the number"))
c2=calendar.month(y,mm)
print(c2)"""
print("1. for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
c=int(input("enter the option"))
a=int(input("enter the number"))
b=int(input("enter the second number"))
if (c==1):
    sum(a+b)
elif(c==2):
    sum(a-b)
elif(c==3):
    sum(a*b)
elif(c==4):
    sum(a/b)
else:
    print("invalid condition")
print("the sum is ",c)
def sum(a,b):
    print("the sum of no",a+b)
    print("the subtraction of the no",a-b)
    print("the multiplication of the no",a*b)
    print("the division of the no",a/b)
sum(a,b)
