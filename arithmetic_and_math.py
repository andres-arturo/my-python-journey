#basic mathmatics functions:

#for rounding a number into an integer:

x = 3.14
y = 4
z = 5
a = -6

result1 = round(x)
print(f'result1 is: {result1}') #this will print 3. Here applies scientific notation. if it were 3.50, it would have printed 4.


result2 = abs(a)
print(f'result2 is: {result2}') #this will print 3 because the ABSOLUTE value of a number is its distance between where it is to 0.

result3 = pow(4, 3) #vulgarmente 4 a la 3... this is 4 to the power of 3... result 64
print(f'result3 is: {result3}')

result4 = max(x, y, z, a)
print(f'result4 is: {result4}') #this will print the maximum value among the 4 variables. This time 5

result5 = min(x, y, z, a)
print(f'result5 is: {result5}') #this will print the minimum value among the 4 variables. This time -6

#for further mathematics operations we will have to import the mathmatics module

import math

f = 9
g = 3.1415926535
i = 12.23

print(math.pi) #--> importar el valor de pi
print(math.e) # --> importar el valor del numero exponencial e
result6 = math.sqrt(f) #--> raíz cuadrada de la variable, en este caso el resultado es 3
print(f'result6 is: {result6}')

result7 = math.ceil(i)
print(f'result7 is: {result7}') #this will print 13. The original value is 12.23 but the ceil function will round up.
#It will show 13.

result8 = math.floor(i)
print(f'result8 is: {result8}') #this will print 12. This will be rounded down no matter what.

result9 = round(g, 4)
print(f'Result9 is: {result9}') #This will show the numbers of decimals you wish and will round up or down
#depending if the value of the limit you set is lower or higher than 5. This time is 3.141592, it will show
#3.1416 because the number 9 was next to .1415 this time.
#Excersise!

#Let's calculate the circumference of a circle!
print("Let's calculate the circumference of your circle.")
radius = float(input("Please enter the radius of your circumference: "))
circumference = 2*math.pi*radius

print(f'The circumference is: {round(circumference, 2)}')


#Let's calculate the area of a circle!

print("Let's calculate the area of a circle!")
radius2 = float(input('Please enter the radius of your circle: '))
area = pow(radius2, 2)*math.pi
print(f'The area of your circle is: {round(area, 2)}')

#Let's calculate the hypotenuse of a triangle!!
print("Let's calculate the Hypotenuse of a right angled triangle!! :D")
adjacent_leg = float(input("Please enter the adjacent leg of your triangle: "))
opposite_leg = float(input("Please enter the opposite leg of your triangle: "))
hypotenuse = math.sqrt(pow(adjacent_leg, 2) + pow(opposite_leg, 2))
print(f'The value of the hypotenuse of your triangle is {round(hypotenuse, 2)}.')