# Checkpoint 4.6
# How many times will 'Hello World' be printed in the 
# following program

count = 10
while count < 1:
    print('Hello World')
print()
# The output does not return a value due to the '<' in while clause.

# Checkpoint 4.15
# What will the following code display?

total = 0
for count in range(1,6):
    total = total + count
print(total)
print()
# Checkpoint 4.16
# What will the following code display?

number1 = 10
number2 = 5
number1 += number2  # same expression as = number1 + number2
print(number1)
print(number2)