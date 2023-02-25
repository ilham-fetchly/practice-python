## Personal practice project ##
## Program to compare the hour input with current hour time ##
from datetime import datetime
print("Welcome to the Daylight Checker.")

name = input('What is your name? ')
print('\nHi ' + name + ', input a number 1 to 24 according to your local time')

# Get the current time
now = datetime.now()
time_hour = now.hour

# Format reference at https://www.geeksforgeeks.org/python-strftime-function/
current_time = now.strftime("%a %b %d,%Y %I:%M %p")

if time_hour == 0:
    time_hour = 24


# Function to convert the string input to the integer value
def input_number():
    input_ = input('What time is it now, ' + name + '? ')
    input_x = float(input_)
    input_time = int(input_x)
    return input_time


# Function to determine the nearby timetable
def nearby_time():
    if time_hour >= 4 and time_hour < 5:
        print("But it's almost morning now!")
    elif time_hour >= 11 and time_hour < 12:
        print("But it's almost afternoon now!")
    elif time_hour >= 16 and time_hour < 17:
        print("But it's almost evening now!")
    elif time_hour >= 21 and time_hour < 22:
        print("But it's almost night now!")
    else:
        None
    print("Current time:", current_time, end="\n")


def start():
    # Input validation
    try:
        input_time = input_number()
    except ValueError:
        print("Wrong input! Please input a number 1 to 24.")
        start()

    # The else-if operator determines the timetable.
    if input_time > 24:
        print("Wrong input! Please input a number 1 to 24")
        start()
    else:
        if time_hour >= 5 and time_hour < 12:
            day = 'morning'
        elif time_hour >= 12 and time_hour < 17:
            day = 'afternoon'
        elif time_hour >= 17 and time_hour < 22:
            day = 'evening'
        else:
            day = 'night'

        if input_time == 0:
            input_time = 24

        if input_time == time_hour:
            print("Right, it's " + str(input_time) + " at " + day + ' now.')
        else:
            print("No, Now it's", time_hour, 'at', day + '!')

        print('Good ' + day + ', ' + name + '!')
        nearby_time()
    restart()


def restart():
    restart = input("\nDo you want to restart the program?(y/n) ")
    if restart == "y" or restart == "Y":
        start()
    else:
        print("Bye,", name + "!")
        exit()


# Starting the program
start()
