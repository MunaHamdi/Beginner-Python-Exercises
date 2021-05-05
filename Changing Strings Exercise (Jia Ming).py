# Write a program that you can read and convert your Numeric inputs into day of the week.
# OR
# Write a programs that can convert number 1 to 7 in integer or text into day of the week? 

def days(num):
    if num == 1:
        return ('Monday')
    elif num == 2:
        return ('Tuesday')
    elif num == 3:
        return ('Wednesday')
    elif num == 4:
        return ('Thursday')
    elif num == 5:
        return ('Friday')
    elif num == 6:
        return ('Saturday')
    elif num == 7:
        return ('Sunday')

num=int(input('Please specify a number: '))
if num <= 7:
    print (days(num))
else:
    print('Sorry, we only have 7 days in a week XD')