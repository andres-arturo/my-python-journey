##if statements.
#These are very fun, but we will see their real power when we start with for and while loops.

name = input('Welcome! Kindly enter your name: ')
length = len(name)

while length <= 1 or length >= 20:
    if length <= 1:
        print("Your name can't have 1 character or be empty .")
        name = input("Enter your name, please: ")
        length = len(name)

    elif length >= 20:
        print("Your name can't have over 19 characters.")
        name = input("Enter your name again, please: ")
        length = len(name)

age = int(input(f'Hi {name}! Thank you for participating in our Credit Card program. Kindly enter your age: '))

while age <=3 or age >=110:
    if age <= 3:
        print(f'Dear {name}, your age cannot be 3 years old or below, else how would you be writing this? Lol.')
        age = int(input(f"Dear {name}, please enter your age, a valid age this time, please: "))
    elif age >= 110:
        print(f"Dear {name}, you can't be over 110 years old, that's impossible. LOL. You wouldn't be able to be writing here by yourself.")
        age = int(input(f"Dear {name}, please enter your age, a valid age this time, please: "))
if age >= 66:
    print(f"I'm sorry {name}, you are too old. You cannot be over 65 years old.")
elif age >= 18:
    print(f"Welcome {name}! You are signed up.")
elif age <= 0:
    print(f'Dear {name}, your age cannot be 0 or below, else you would have been born yet.')
else:
    print(f'dear {name}, unfortunately, you must be over 18 years old to sign up.')



