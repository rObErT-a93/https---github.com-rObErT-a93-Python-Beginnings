print('One')
print('Two')
print('Three')

print('One', end=' ')
print('Two', end=' ')
print('Three', end=' ')

print('One', end='')
print('Two', end='')
print('Three')

print('One', 'Two', 'Three', sep='~~~')

print('One\nTwo\nThree')

print('Mon\tTues\tWed')
print('Thur\tFri\tSat')

print("Your assignment is to read \"Hamlet\" by tomorrow.")
print('I\'m ready to begin.')

print('The path is C:\\temp\\data.')

print('This is ' + 'one string.')

print('Enter the amount of ' + 'sales for each day and ' + 'press Enter.')

# This program demonstrates how a floating-point
# number is displayed  with no formatting.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print('The monthly payment is', monthly_payment)

print(format(416.666666667, '.2f'))
print(format(416.666666667, '.1f'))
print('The monthly payment is', format(416.666666667, '.2f'))

amount_due = 5000.0
monthly_payment = amount_due / 12
print('The monthly payment is',
    format(monthly_payment, '.2f'))

print(format(416.666666667, 'e'))
print(format(416.666666667, '.2e'))

print(format(416.666666667, 'E'))
print(format(416.666666667 , '.2E'))

print(format(12345.6789, ',.2f'))

print(format(123456789.456, ',.2f'))
print(format(12345.6789, ',f'))

# This program demonstrates how a floating-point
# number can bedisplayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $',
    format(annual_pay, ',.2f'),
        sep='')

print('The number is', format(12345.6789, '12,.2f'))

print("The number is", format(12345.6789, '12.2f'))

# This program displays the following
# floating-point numbers in a column
# with their decimal points aligned.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Display each number in a field of 7 spaces
# with 2 decimal places.
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))
print(format(0.5, '%'))
print(format(0.5, '.0%'))

print(format(123456, 'd'))
print(format(123456, ',d'))
print(format(123456, '10d'))
print(format(123456, '10,d'))

INTEREST_RATE = 0.069
balance = 123456
amount = balance * INTEREST_RATE
print(format(amount, '10.2f'))

# Code from YouTube
90
import colorsys
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
h = 4
for i in range(300):
    c = colorsys.hls_to_rgb(h, 0.5, 0.9)
    t.pencolor(c)
    h += 0.005
    t.circle(100, 200)
    t.circle(50, 200)

    for j in range(4):
        t.rt(90)
        t.forward(20)
    t.hideturtle()
turtle.done()
