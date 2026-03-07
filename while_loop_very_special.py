username = input("Please enter a username: ")

# Keep looping as long as ANY condition is failed
while len(username) < 6 or len(username) > 12 or not username.isalpha():
    if len(username) < 6 or len(username) > 12:
        print("Sorry, your name must be between 6 and 12 characters.")
    elif not username.isalpha():
        print("Sorry, your name must be letters only (no numbers, spaces, or symbols).")

    # You only need to ask for the input ONCE at the end of the loop
    username = input("Please enter a username: ")

print(f"Your username has been created successfully: {username}")