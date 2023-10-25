''' Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.'''

#user input
a = int(input("Enter the value for a : "))
b = int(input("Enter the value for b : "))
c = int(input("Enter the value for c : "))

if a==b or b==c or a==c :
    sum=0
else:
    sum = a+b+c   
print(sum)