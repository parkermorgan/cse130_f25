# 1. Name:
#      Parker Morgan
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      The program prompts for a start and end date, validates the input,
#      adjusts for leap years, computes the total days between the dates, and 
#      displays the result to the user. 
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out how to translate my pseudocode
#      of calculating the start_day_num and end_day_num. It was nice to have 
#      the foundation of my initial design, but taking that and turning it into
#      python took me a while. Once I was able to do it for the start_day_num,
#      it made it much easier to complete it for end_day_num. I also had a hard 
#      time figuring out where to put my asserts. I initially was going to put
#      some for the user inputs, but that would cause the loop to end and crash
#      the whole program, and my loops for error handling already covered it, 
#      so I found it redundant to put asserts there. 
# 5. How long did it take for you to complete the assignment?
#      This assignment took me approximately 1 hour and 45 minutes. 

# Function to determine leap year.
def is_leap_year(year):
    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    assert isinstance(result, bool), (
        'is_leap_year must return true or false'
    )
    return result

def calculate_days():
    # Start date prompts and loops.
    while True:
        try:
            start_year = int(input('Start year: '))
        except ValueError:
            print('Invalid input. Please enter an integer for year.')
            continue
        if start_year < 1753:
            print('Invalid year. Year must be 1753 or later.')
            continue
        break

    while True:
        try:
            start_month = int(input('Start month: '))
        except ValueError:
            print('Invalid input. Please enter an integer for month.')
            continue
        if start_month < 1 or start_month > 12:
            print('Invalid month. Month must be between 1 and 12.')
            continue
        break
    
    # Determine date of February if it is a leap year.
    start_month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(start_year):
        start_month_lengths[1] = 29
        days_start_year = 366
    else:
        days_start_year = 365
    assert (
        days_start_year in (365, 366)
    ), 'days_start_year must be 365 or 366'

    while True:
        try:
            start_day = int(input('Start day: '))
        except ValueError:
            print('Invalid input. Please enter an integer for day.')
            continue
        if start_day < 1 or start_day > start_month_lengths[start_month - 1]:
            print(
                f'Invalid day. Day must be between 1 and '
                f'{start_month_lengths[start_month - 1]}.'
            )
            continue
        break

    # End date prompts and loops.
    while True:
        try:
            end_year = int(input('End year: '))
        except ValueError:
            print('Invalid input. Please enter an integer for year.')
            continue
        if end_year < 1753:
            print('Invalid year. Year must be 1753 or later.')
            continue
        break

    while True:
        try:
            end_month = int(input('End month: '))
        except ValueError:
            print('Invalid input. Please enter an integer for month.')
            continue
        if end_month < 1 or end_month > 12:
            print('Invalid month. Month must be between 1 and 12.')
            continue
        break

    end_month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(end_year):
        end_month_lengths[1] = 29

    while True:
        try:
            end_day = int(input('End day: '))
        except ValueError:
            print('Invalid input. Please enter an integer for day.')
            continue
        if end_day < 1 or end_day > end_month_lengths[end_month - 1]:
            print(
                f'Invalid day. Day must be between 1 and '
                f'{end_month_lengths[end_month - 1]}.'
            )
            continue
        break
        
    # Calculate the total count of start_day
    start_day_num = 0
    for start_month_index in range(0, start_month - 1):
        assert (
            0 <= start_month_index < 12
        ), 'start_month_index out of range'
        start_day_num = start_day_num + start_month_lengths[start_month_index]
    start_day_num = start_day_num + start_day
    assert (
        1 <= start_day_num <= days_start_year
    ), 'start_day_num out of range'

    # Calculate days left in year for start date.
    start_days_left = days_start_year - start_day_num
    assert (
        start_days_left >= 0
    ), 'start_days_left must be non-negative'

    # Calculate the total count of end_day
    end_day_num = 0
    for end_month_index in range(0, end_month - 1):
        assert (
            0 <= end_month_index < 12
        ), 'end_month_index out of valid range'
        end_day_num = end_day_num + end_month_lengths[end_month_index]
    end_day_num = end_day_num + end_day

    # Check end_day_num range.
    if is_leap_year(end_year):
        assert (
            1 <= end_day_num <= 366
        ), 'end_day_num out of range for leap year'
    else:
        assert (
            1 <= end_day_num <= 365
        ), 'end_day_num out of range for non-leap year'

    # Check if end date is before start date. 
    if end_year < start_year:
        print('End date must not be before start date.')
        return
    elif end_year == start_year and end_day_num < start_day_num:
        print('End date must not be before start date.')
        return
    
    # Check if dates are the same
    if start_year == end_year and start_month == end_month and start_day == end_day:
        print('Dates cannot be the same.')
        return

    # Special case if the dates are in the same year.
    if start_year == end_year:
        number_of_days = end_day_num - start_day_num
        assert (
            number_of_days >= 0
        ), (
            'number_of_days must be non-negative when start_year == end_year'
        )
        print(f'The number of days between the two dates is: {number_of_days}')
        return

    # Calculate number of days between.
    days_years_between = 0
    for year in range(start_year + 1, end_year):
        if is_leap_year(year):
            days_years_between = days_years_between + 366
        else:
            days_years_between = days_years_between + 365
    assert (
        days_years_between >= 0
    ), 'days_years_between must be non-negative'

    number_of_days = start_days_left + days_years_between + end_day_num
    assert (
        number_of_days >= 0
    ), 'number_of_days must be non-negative'

    # Display number of days to user. 
    print(f'There are {number_of_days} days between the two dates.')

calculate_days()
