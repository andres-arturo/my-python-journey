

print("Weight converter.")
print("You can convert from Pounds to Kilograms and vice versa. :)")


weight = input("Please enter the weight: ")
weight_is_number_only = weight.replace(".", "").isdigit()

while not weight_is_number_only:
    print("The weight must be numbers only. Please try again.")
    weight = input("Please enter the weight: ")
    weight_is_number_only = weight.replace(".", "").isdigit()

unit = input("Please enter the unit you wish to (Lb or Kg): ")
unit = unit.lower()

while unit != "lb" and unit != "kg":
    print("Please enter a valid unit. Remember: MUST BE KG OR LB.")
    unit = input("Please enter the unit you wish to (Lb or Kg): ")
    unit = unit.lower()

weight = float(weight)

if unit == "lb":
    result = weight / 2.20462
    print(f"{weight}lbs is {round(result, 2)}kg.")
elif unit == "kg":
    result = weight * 2.20462
    print(f"{weight}kg is {round(result, 2)}lbs")