# PCC Try It Yourself 5-8. Hello Admin, 5-9. No Users

usernames = []#'jim', 'angela', 'chris', 'bobby', 'michelle', 'admin', 'chell']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")