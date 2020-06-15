# PCC Try It Yourself 8-10. Sending Messages.

def send_messages(messages):
    """Displays a message and moves it to a sent message list"""
    while messages:
        sent_message = messages.pop()
        print(sent_message)
        sent_messages.append(sent_message)

sent_messages = []
messages = [
            "There's gold in them thar hills.",
            "There's a snake in mah boots!",
            "Howdy pardner.",
            "How's about a good ol' fashioned hoedown?",
            ]

#send_messages(messages)

# Check the lists to make sure everything moved properly.
#print(messages)
#print(sent_messages)

# 8-11. Archived Messages.
send_messages(messages[:])

# Check the lists to make sure the original is intact.
print(messages)
print(sent_messages)
