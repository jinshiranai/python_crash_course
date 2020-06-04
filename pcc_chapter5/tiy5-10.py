# PCC Try It Yourself 5-10. Checking Usernames

current_users = ['jim', 'ashley', 'chris', 'nathaniel', 'Emily']
current_users_lowercase = []

for current_user in current_users:
    current_users_lowercase.append(current_user.lower()) 

new_users = ['clayton', 'ash', 'CHRIS', 'bobby', 'emily']

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print("Sorry, that username is unavailable. Please enter a different username.")
    else:
        print("That username is available.")