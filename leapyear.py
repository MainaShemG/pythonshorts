year=int (input('Enter a year: ' ''))
#prompts user to enter the year they wish to check if it is leap

if (year % 400 == 0) and ( year % 100 == 0):
    print('{0} is a leap year'.format(year))

elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))
