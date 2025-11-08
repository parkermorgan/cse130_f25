

#Problem 0.6.1
def average_gpa(gpas):  
    ''' Find the average GPA from the list '''

    # Add them up.
    sum = 0
    for gpa in gpas:
        sum += gpa

    # Compute the average and return.
    average = sum / len(gpas)
    return average



#Problem 0.6.3
def display_grade(grade):  
    ''' Break a grade such as "A+" into "A" and "+" '''
    letter = grade[0]
    sign   = grade[1]
 
    print("Your letter grade is", letter, "and your sign is", sign)
 



#Problem 0.6.4
def compute_tax (income):
    ''' Compute the tax burden based on income. '''
    tax = -1.0 

    # 10% bracket.
    if 0 <= income < 15100:
        tax = income * 0.10
    # 15% bracket.
    elif 15100 <= income < 61300:
        tax = 1510 + 0.15 * (income - 15100)
    # 25% bracket.
    elif 61300 <= income < 123700:
        tax = 8440 + 0.25 * (income - 61300)
    # 28% bracket.
    elif 123700 <= income < 188450:
        tax = 24040 + 0.28 * (income - 123700)
    #33% bracket.
    elif 188450 <= income < 336550:
        tax = 42170 + 0.33 * (income - 188450)
    #35% bracket.
    elif income >= 336550:
        tax = 91043 + 0.35 * (income - 336550)
    return tax



#Problem 0.6.5
def binary_search(array, search):
    ''' Return TRUE if search exists in array. '''

    # Initialize the bounding indices.
    i_first = 0
    i_last = len(array) - 1

   # Continue as long as there are elements in the range.
    while i_first <= i_last:
        i_middle = (i_first + i_last) // 2

       # Too high or too low.
        if array[i_middle] < search:
            i_first = i_middle + 1
        elif array[i_middle] > search:
            i_last = i_middle - 1

        # Found!
        else:
            return True

    # Not found!
    return False



#Problem 0.6.6
def compute_tax(income):
    ''' Compute the tax burden based on income. '''
    brackets = [
    # min max fixed rate 
        ( 0, 15100, 0, 0.10),
        ( 15100, 61300, 1510, 0.15),
        ( 61300, 123700, 8440, 0.25),
        (123700, 188450, 24040, 0.28),
        (188450, 336500, 42170, 0.33),
        (336500, 99999999, 91043, 0.35)
    ]

    for bracket in brackets:
        if bracket[0] <= income and bracket[1] >= income:
            return bracket[2] + bracket[3] * (income - bracket[0])
    return 0.0