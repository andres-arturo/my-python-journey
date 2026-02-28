



#Let's convert  Kilograms to Pounds and viceversa!
print("Hi! Welcome to this weight converter. You can convert Pounds to Kilograms or Kilograms to Pounds for free!")
weight = float(input("Please enter the weight you wish to convert: "))
unit = input("Please enter the unit of your weight, it will automatically be converted to the other one: ")

if unit == "kg":
    weight = weight * 2.205
    print(f'Your weight in Pounds is: {round(weight, 2)}lbs')

elif unit == "lbs":
    weight = weight / 2.205
    print(f'Your weight in Kilograms is: {round(weight, 2)}kg')

else:
    print("You did not enter a valid unit.")


#Let's convert Celsius to Fahrenheit and vice versa!

print("Hi! Welcome to this temperature converter. You can convert Celsius to Fahrenheit and vice versa for free!")
temperature = float(input("Please enter the temperature: "))
unit2 = input("Please enter the unit (C o F): ")

if unit2 == "C":
    temperature = round((temperature*9/5) + 32, 2)
    print(f"The temperature in Fahrenheit is {temperature}F")

elif unit2 == "F":
    temperature = round((temperature - 32) * 5/9, 2)
    print(f"The temperature in Celsius is {temperature}C")

else:
    print("You did not enter a valid unit of temperature.")