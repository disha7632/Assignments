'''Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.
'''

 #Taking input from the user
inputString = "Tpops technologies"
 
count = 0
 
# Loop through the string
for i in inputString:
      count = count + 1
newString = inputString[ 0:2 ] + inputString [count - 2: count ] 
 
# Printing the new String
print("Input string = " + inputString)
print("New String = "+ newString)
