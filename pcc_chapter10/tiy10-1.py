# PCC Try It Yourself 10-1. Learning Python.

filename = '/home/jin/python_work/python_crash_course/pcc_chapter10/learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
print(contents.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# PCC Try It Yourself 10-2. Learning C.
with open(filename) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())