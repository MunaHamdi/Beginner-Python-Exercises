# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. (NEED TO INPUT PLACE)
# If the string length of the given string is less than 3, leave it unchanged.


data=input('Please indicate a word: ')
strlength=len(data)
#print(strlength)

lyexist=data.find('ing')
#print(lyexist)

if lyexist != -1 and lyexist == (strlength-3):
    new=data[0:lyexist]
    #print(new)
    word=(new+'ly')
    print(word)
    x=(strlength-3)
elif len(data) < 3:
    print(data)
elif len(data) >= 3:
    print(data+'ing')

#ADDITIONAL: Write a Python program to count repeated characters in a string.

word=data
count=0

for key in word:
    if key == 't':
        count=count+1
print(count)