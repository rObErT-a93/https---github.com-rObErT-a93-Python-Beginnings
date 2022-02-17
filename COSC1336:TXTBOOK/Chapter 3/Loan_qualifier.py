# PROGRAM 3-5: LOAN QUALIFIER_1
# This program determines whether a bank custeomer
# qualifies for a loan.

MIN_SALARY = 30000.0 # the minimum annual salray
MIN_YEARS = 2        # the minimum years on the job
print()
# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of' + 
                        ' years emplyed: '))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed',
        'for at least', MIN_YEARS,
        'years to qualify.')
else:
        print('You must earn at least $',
        format(MIN_SALARY, ',.2f'),
        ' per year to qualify.', sep='')
print()
# Program 3-6: GRADER.PY
# This program gets a numeric test score from
# user and displays the corresponding letter grade.

# Named constants to represent the grade thresholds
A_Score = 90
B_Score = 80
C_Score = 70
D_Score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade.

if score >= A_Score:
    print('Your grade is A.')
else:
    if score >= B_Score:
        print('Your grade is B.')
    else:
     if score >= C_Score:
         print('Your grade is C.')
     else: 
        if score >= D_Score:
            print('Your grade is D.')
        else:
            print('Your grade is F.')