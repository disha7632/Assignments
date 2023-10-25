'''Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.
'''

string=input("enter the string:")
length=len(string)
if length>=3:    
    if string[-3:]=='ing':
        new=string+'ly'
        print(new)
    else:
        new=string+'ing'
        print(new)
else:
    print("will not change:",string)