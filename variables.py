#Variables = Are used to store data. Some types are: Strings, Integers, Float, and Booleans

#Strings
first_name = "Andres"
favorite_food = "pizza"

print(first_name)

name = input("Please enter your name: ")

print(f'Hi {name}!')

print(f'Hi {first_name}, your favorite food is {favorite_food}.')

#Integers
#are just numbers, with no decimals.

age = 30

print(f'Hi {first_name}, your favorite food is {favorite_food} and your age is {age}.')

#Float
#are just numbers, but with decimals this time.

rice_price = 3.99
tv_price = 200
print(f'Hi {first_name}, the price of the rice is ${rice_price}.')

#Booleans
#It will show if it is true or false if we print it just as it is.
#However, this has different uses, and it can become tricky, BUT IT IS AWESOME IF WE USE IT CORRECTLY!!

is_student = False
for_sale = False

if is_student:
    print(f'Hi {first_name}, welcome!')
else:
    print(f'Hey, Im sorry but you are not allowed to enter because you are not a student.')

if for_sale:
    print(f'Hi, the price of the TV is ${tv_price}.')
else:
    print(f'Im sorry, the tv has been sold already')



