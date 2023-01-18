# Leap year calculator.

#function to loop an input
def loop(actual_input, arguments, error_message,lower,int_ch):
    arguments = list(arguments)
    if lower == True:
        while True:
            print(" ")
            x = input(actual_input).strip().lower()
            if x in arguments:
                if int_ch:
                    if x.isdigit():
                        break
                    else:
                        print("Please enter a number")
                        continue
                else:
                    break
            else:
                print(" ");print(error_message)
        if int_ch:
            return int(x)
        else:
            return x
    elif lower == False:
        while True:
            print(" ")
            x = input(actual_input).strip().lower()
            if len(x) == 0:
                print("Please enter the required details.")
            else:
                if int_ch:
                    if x.isdigit():
                        break
                    else:
                        print("Please enter a number")
                        continue
                break
        if int_ch:
            return int(x)
        else:
            return x

def leap_check():
    print(" ")
    year = loop("Enter the year: ", [None], " ", False,True)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

    user()

def leap_range():
    starting = loop("Enter the starting year: ", [None], " ", False,True)
    ending = loop("Enter the ending year: ", [None], " ", False,True)
    x = 0
    year = []
    for i in range(starting, ending + 1):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            year.append(i)
            x += 1
    print(f"There are {x} leap year(s) between {starting} to {ending}")
    ask = loop("Would to like to see the years (y/n): ", ["y", "n"], "Please enter 'Y' or 'N'", True,False)
    if ask  == "y":
        for x in year:
            print(x)
    else:
        print("Ok sure no problem")
    user()

def leap_period():
    year_sta = loop("Enter the current year: ", [None], " ", False, True)
    year = loop("Enter the number of years: ", [None], " ", False, True)
    year1 = year_sta + year
    leap_year = 0
    t_year = []
    for i in range(year_sta, year1 + 1):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            t_year.append(i)
            leap_year += 1
    print(f"There are {leap_year} leap year(s) between {year_sta} to {year1}")
    ask = loop("Would to like to see the years (y/n): ", ["y", "n"], "Please enter 'Y' or 'N'", True, False)
    if ask == "y":
        for x in t_year:
            print(x)
    else:
        print("Ok sure no problem")
    user()

def leap_next():
    starting = loop("Enter the current year: ", [None], " ", False, True)
    n = 1
    while True:
        test = starting + n
        if test % 4 == 0 and (test % 100 != 0 or test % 400 == 0):
            break
        else:
            n +=1
    print(f"{starting + n} is the next leap year")
    user()
def user():
    user_ans = input('''
Enter
'1') To check if the given year is a leap year or not. 
'2') To find the leap years between the given years.
'3)' To find the number of leap years from 2020 to the given period of years.
'4)' To check when is the next leap year
'5)' TO end the programme
: ''').strip()

    if user_ans == "1":
        leap_check()
    elif user_ans == "2":
        leap_range()
    elif user_ans == "3":
        leap_period()
    elif user_ans == "4":
        leap_next()
    elif user_ans == "5":
        quit()
    else:
        print("Invalid option!")
        user()

user()
