name1 = 'Robert'
name2 = 'Bobby'
print()
if name1 == name2:
    print('The names are the same.')
else:
    print('The names are NOT the same.')
print()

name3 = 'Robert'
name4 = 'Robert'

if name3 == name4:
    print('The names are the same.')
else:
    print('The names are NOT the same.')

print()
# Password Exercise 3-3
password = input('Enter password here: ')
if password == 'prospero':
    print('Password Accepted.')
else:
    print('Incorrect Password Entered.')
print()
# Sorting Names Exercise 3-4
name1 = input('Enter a name ( last name first): ')
name2 = input('Enter another name ( last name first): ')
print()
print('Here are the names, listed alphabetically.')

if name1 < name2:
    print(name1)
    print(name2)

else:
    print(name2)
    print(name1)
print()
