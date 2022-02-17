#3.11 What would the following code display?
if 'z' < 'a':
    print('z is less than a')
else:
    print('z is not less than a')
print()

#3.12 What would the following code display?
s1 = 'New York'
s2 = 'Boston'
if s1 > s2:
    print(s2)
    print(s1)
else:
    print(s1)
    print(s2)
print()

#3.13 Write an if-elif-else statement
number = int(input('Enter a number: '))
if number == 1:
    print('One')
elif number == 2:
    print('Two')
elif number == 3:
    print('Three')
else:
    print('Unknown entry')
print()

#3.18 Write an 'if' statement that displays the message "the number is valid"
# if the the value referenced by "speed" is w/n the range 0 thru 200
speed = 175
if speed >= 0 and speed <= 200:
    print('The number is valid')
else:
    print('The number is not valid')
print()

#3.19 Write an 'if' statement that displays the message "The number is not valid"
# if the value referenced by "speed" is outside the range 0 thru 200
speed2 = 201
if speed2 >= 0 and speed2 <= 200:
    print('The number is valid')
else:
    print('The number is not valid')