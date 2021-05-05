# Given a string, S , of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

# Input Format

# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a string, S.

# Constraints
# 1 <= T <= 10
# 2 <= length of S <= 1000

# Output Format

# For each String, Sj (where 0 <= j <= T-1 ), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.

T=input('Enter no. of test cases: ')

for i in range(int(T)):
    odd=''
    even=''
    
    S=input('What is your string: ')
    N=len(S)
    index=0
      
    while index < len(S):
        letter=S[index]
        if (index%2) == 0:
            odd+=letter
            #print(index, letter, 'odd')
        else:
            even+=letter
            #print(index, letter, 'even')
        index=index+1
    print(even,odd)
    

   
        


    