# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.


data=input('Please indicate a word: ')
strlength=len(data)
#print(strlength)

lyexist=data.find('ing')
print(lyexist)
if lyexist != -1:
    word=data.replace('ing','ly')
    print(word)
elif len(data) < 3:
    print(data)
elif len(data) >= 3:
    print(data+'ing')

