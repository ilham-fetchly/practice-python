## Personal practice project ##
## Program to compare the hour input with current hour time ##
print("Welcome to the Daylight Checker.")

from datetime import datetime
name = input('What is your name? ')

def start():
    # Get the current time
    now = datetime.now()
    time_hour = now.hour
    # Format the date and time using strftime function
    # Format reference at https://www.geeksforgeeks.org/python-strftime-function/
    current_time = now.strftime("%a %b %d,%Y %I:%M %p")
    print('\nHi ' + name + ', input numbers 1 to 24 according to your local time')
    # Convert the string input to the integer value using the 'int' method
    input_time = int(input('What time is it now, ' + name + '? '))

    # The else-if operator determines the timetable.
    if time_hour >= 5 and time_hour < 12:
        day = 'morning'
    elif time_hour >= 12 and time_hour < 17:
        day = 'afternoon'
    elif time_hour >= 17 and time_hour < 22:
        day = 'evening'
    else: day = 'night'

    # Function to determine the nearby timetable
    def nearby_time():
        print('Good ' + day + ', ' + name + '!')
        if time_hour >= 4 and time_hour < 5:
            print("But it's almost morning now!")
        elif time_hour >= 11 and time_hour < 12:
            print("But it's almost afternoon now!")
        elif time_hour >= 16 and time_hour < 17:
            print("But it's almost evening now!")
        elif time_hour >= 21 and time_hour < 22:
            print("But it's almost night now!")
        else: None
        print("Current time:", current_time, end="\n")

    if time_hour == 0:
        time_hour = 24

    if input_time == 0:
        input_time = 24

    if input_time == time_hour:
        print("Right, it's " + str(input_time) + " at " + day + ' now.')
    else:
        print("No, Now it's", time_hour, 'at', day + '!', end=' ')

    nearby_time()
    restart_app()

def restart_app():
    restart = input("\nDo you want to restart the program?(y/n) ")
    if restart == "y" or restart == "Y":
        start()
    else: print("See you")

# Starting the program
start()