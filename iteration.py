#simple if statement
'''x = int(input('Enter number: '))
if x % 2 == 0:
    print('it is a even number')
elif x % 2 != 0:
    print('not even number')
else:
    print('try again')'''

#for loop with range and while
'''numbers = [3,4,5,6,8,0,2,1,7,5]

for i in range(len(numbers)):
    print('your range is:', numbers[i])'''

#print a range
'''print(range(10))
print(list(range(10)))
print(list(range(2,9)))
# range(start, stop,step_size)
print((list(range(2,20,4))))'''

#for with else
# program to display student's marks from record
''''student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')'''

#While loop
i=int(input('Enter number: '))
while i<10:
    print('it is a good number')


else: print('i is less than 10' )