
#Logical Operators = Evaluate multiple conditions (or, and, not)
                    #or = at least  one of the conditions must be true.
                    #and = both conditions must be true.
                    #not = inverts the condition (not False, not True).

#Examples with "or":
temp = 36
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")

else:
    print("The outdoor event is still scheduled.")

print("___________________________________________")

temp = 30
is_sunny = False

if temp > 28 and is_sunny:
    print("It is hot outside.")
    print("Today is a Sunny Day!!")
elif temp < 0 and is_sunny:
    print("It is cold outside.")
    print("But hey, today is a sunny day!")
elif temp <= 28 and temp >= 0 and is_sunny:
    #Other way:
    #elif 28 > temp > 0 and is_sunny:
    print("The weather is neither too cold nor too hot!")
    print("And hey!!! IT IS SUNNY :D")
elif temp <= 28 and temp >= 0 and not is_sunny:
    # Other way:
    # elif 28 > temp > 0 and not is_sunny:
    print("The weather is neither too cold nor too hot!")
    print("And hey!!! It is CLOUDY!! :D")
elif temp > 28 and not is_sunny:
    print("It is hot outside...")
    print("And it is cloudy!!")
elif temp < 0 and not is_sunny:
    print("It is cold outside.")
    print("But hey, today is a cloudy day! Meaning that the day will feel even colder HAHA!")