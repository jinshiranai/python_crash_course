# Code demonstrating accessing a file.
# For some reason this code is actually running elsewhere so...
# Straight to absolute pathing we go.

filename = '/home/jin/python_work/python_crash_course/pcc_chapter10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

# Is you birthday in the first million digits of pi?
birthday = input("Enter your birthday, in the format mmddyy: ")
if birthday in pi_string:
    print("You birthday is in the first million digits of pi!")
else:
    print(" Your birthday is not in the first million digits of pi.")