

username = input("Please enter a username: ")

while len(username) > 12 or len(username) < 6 or not username.isalpha():
    if len(username) > 12 or len(username) < 6:
        print("Sorry, your name must be between 6 and 12 characters.")


    elif not username.isalpha():
        print("sorry, your name must be letters only, no numbers or special digits are allowed.")
    username = input("Please enter a username: ")

print(f"Your username has been created successfully. Your username: {username}")