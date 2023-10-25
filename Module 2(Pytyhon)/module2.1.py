# Write a Python program to check if a number is positive, negative or zero.

#user input
number = int(input("Enter the number:"))

if number==0:                          #condition
    print("Number is zero")            #statement

elif number > 0:
    print("The entered number is positive.")

elif number < 0:
    print("The entered number is negative.")    

else:
    print("please enter number.")    

