# Code to emphasize writing clear prompts.

name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!\n")

# Building a prompt over several lines.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name.title()}!")