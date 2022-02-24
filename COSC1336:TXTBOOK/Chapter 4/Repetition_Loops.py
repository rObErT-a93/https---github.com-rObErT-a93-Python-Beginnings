# Program 4-1 Commission
# This program calculates sales commisions.
print()
# Create a variable to control the loop.
keep_going = 'y'

# Calculoate a series of commissions.
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    
    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print('The Commission is $',format(commission, ',.2f'), sep='')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' + 'commission (Enter y for yes): ')
print()

# Program 4-2 Temperature
# This program assists a technician in the process of checking
# a substance's temperature.

# Named constant to represent the maximum temperature.
MAX_TEMP = 102.5

# Get the substance's temperature.
temperature = float(input("Enter the substance's Celsius temperature: "))

# As long as necessary, instruct the user to adjust the thermostat.
while temperature > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    print()
    temperature = float(input('Enter the new Celsius temperature: '))

# Remind the user to check the temperature again in 15 minutes.
print('The temperature is acceptable.')
print('Check it again in 15 minutes.')
print()

# Program 4-3: Infinite Loop
# This program demonstrates an infinite loop
# Create a variable to control the loop.
keep_going2 = 'y'

# WARNING! INFINITE LOOP!
# while keep_going2 == 'y':
    # Get a salesperson's sales and commission rate.
    #sales = float(input('Enter the amount of sales: '))
    #comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    #commission = sales * comm_rate

    # Display the commission.
    #print('The commission is $', format(commission, ',.2f'), sep='')
print()

# Program 4-4: Simple Loop
# This program deomonstrates a simple for loop
# that uses a list of numbers.

print('I will display the numbers 1 through 5.')
for num in [1,2,3,4,5]: # num = variable (target variable), followed by sequence of data items as a value
                        # which will be assigned to variable each iteration
    print(num)
print()

# Program 4-5: Simple Loop 2
# This program alos demonstrates a simple for loop
# that uses a list of numbers.

print('I will display the odd numbers 1 through 9.')
for num in [1,3,5,7,9]:
    print(num)
print()

# Program 4-7: Simple Loop 4
# This program demonstrates how the range function
# can be used with a for loop.

# Print a message five times.
for x in range(5):  # same as 'for num in [0,1,2,3,4]'
    print('Hello World')
print()

# Program 4-8 Squares
# This program uses a loop to display a
# table showing the numbers 1 through 10 and their squares.

# Print the table headings.
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their squares.
for number in range(1,11):
    square = number**2
    print(number, '\t', square)