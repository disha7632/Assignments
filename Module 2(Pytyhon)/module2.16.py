'''Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

string="not poor the movie was"
if string.startswith("not poor"):    
    new=string.replace("not poor","good")   #replacing not poor with good
    print(new)
else:
    print(string)


'''if 'not poor' in string:
    new=string.replace("not poor","good")   #replacing not poor with good
    print(new)
else:
    print(string)'''