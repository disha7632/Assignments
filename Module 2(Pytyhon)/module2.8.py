'''Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5.
'''
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
sum=a+b
print("sum is:",sum)
diff=a-b
print("difference is:",diff)
if a==b or sum==5 or diff==5:
    print("true")
else:
    print("False")