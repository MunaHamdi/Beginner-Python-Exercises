# The provided code stub reads and integer, n , from STDIN. For all non-negative integers i<n , print i**2.

#cInput Format

# The first and only line contains the integer, n.

# Constraints
# 1 <= n <= 20

# Output Format

# Print n lines, one corresponding to each i. 

n = int(input('Give me a number: '))

#if (1 <= n <= 20):
#    while ( n > 0):
#        n=n-1
#        print(n**n)

if (1 <= n <= 20):
    for x in range(0,n):
        print(x**x)