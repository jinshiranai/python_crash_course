# Code demonstrating the input() function.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Letting the user choose when to quit.
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)

# Using a flag.
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)