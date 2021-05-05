T=int(input('Select test case no: ')) #Number of test cases 1-10
test_cases=[]
for i in range(T):
    test_cases.append(input('Indicate your desired string: '))
print(test_cases)


r=s[::-1]

for i in range(1, len(s)):
    if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(r[i])-ord(r[i-1])):
        return("Not Funny")
    return('Funny')