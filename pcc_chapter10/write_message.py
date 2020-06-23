# Code demonstrating writing to a file.

filename = 'programming.txt'

#with open(filename, 'w') as file_object:
#    file_object.write("I love programming!\n")
#    file_object.write("I love creating new games!\n")


# Appending to a file.
with open(filename, 'a') as file_object:
    file_object.write("I love finding meaning in large datasets!\n")
    file_object.write("I love creating apps that can run in a browser!\n")
    file_object.write("I love bringing the corrupt to justice!\n")

with open(filename) as file_object:
    print(file_object.read())