# Conditional expressions = A one line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of 2 values based on a condition
#                           X if condition else Y


num1 = 6
num2 = 4
age = 17
print("Your number is higher than 6 :)" if num1 > 6 else "less than 6 :(")
result = "Even" if num2 % 2 == 0 else "Odd"
print(result)
max_num = num1 if num1 > num2 else num2
min_num = num1 if num1 < num2 else num2
print(max_num)
print(min_num)
status = "Welcome!" if age > 17 else "You are not an adult. Sorry."
print(status)