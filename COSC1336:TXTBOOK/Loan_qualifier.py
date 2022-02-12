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