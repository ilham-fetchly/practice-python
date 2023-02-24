#Write your code below this line 👇
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("-----------")
# Manipulate 3 lines of the print method to one line print method 
# by adding \n at every end of the paragraph
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

print("-----------")
# Different ways to concatenate the strings
print("Hello", "Ilham")
print("Bonjour " + "Ilham")
print("Hola" + " " + "Ilham")
print("Olá" + " Ilham")

print("-----------")
# Input function
print(input("Type your greeting words: "))

print("-----------")
# Variables
name = "Ilham"
age = 25
weight_kg = 48.5
my_city = "Bali"
hobby1 = "coding"
hobby2 = "gaming"

# Convert integer to string and combine it into string output
print("My name is " + name + ", and I'm " + str(age) + " years old.")

# Combine string and number into the output 
# and combine 2 print output become one output
print("I live in", my_city + ", my weight is", weight_kg, "kg, ", end='and ')
print("my hobbies are " + hobby1 + " and " + hobby2 + ".")

print("-----------")
## Program to compare the hour input with current hour time ##
print("Welcome to the Daytime Checker.")
# Get an hour of the current time
from datetime import datetime
time_hour = datetime.now().hour
now = datetime.now()
# Format the date and time using strftime function
# Format reference at https://www.geeksforgeeks.org/python-strftime-function/
current_time = now.strftime("%a %b %d,%Y %I:%M %p")

# Input method
name = input('What is your name? ')
print('Hi ' + name + ', input numbers 1 to 24 according to your local time')
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
    print("Current time:", current_time)

if time_hour == 0:
    time_hour = 24

if input_time == 0:
    input_time = 24

if input_time == time_hour:
    print("Right, it's " + str(input_time) + " at " + day + ' now.')
else:
    print("No, Now it's", time_hour, 'at', day + ',' ,name + '!', end=' ')

nearby_time()
