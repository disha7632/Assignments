# Write a Python program to get the Factorial number of given number.

#user input
num = int(input("Enter the number: "))

#variable value
factorial = 1

if num==0:                                               #condition
    print("the factorical of 0 is 1.")                   #statement

elif num<0:
    print("sorry,factorial does not exist for negative numbers.")

else:
    for i in range(1,num+1):
     factorial = factorial*i
    print(f"The factorial of {num} is {factorial}") 
