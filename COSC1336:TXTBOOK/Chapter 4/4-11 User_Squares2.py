# This program uses a loop to display a 
# table of numbers and their squares.
print()
# Get the startign value.
print('This program displays a list of numbers')
print('and their squares.')
start = int(input('Enter the starting number: '))

# Get the ending limit.
end = int(input('How high should I go? '))

# Print the table heading.
print()
print('Number\tSquare')
print('--------------')

# Print the numbers and their squares.
for number in range(start, end + 1):
    square = number **2
    print(number, '\t', square)
print()