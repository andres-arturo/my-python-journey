#nested loop = A loop within another loop (outer, inner)
                    #outer loop:
                        #inner loop:

for y in range(3): #This will execute the loop (n) times.
    for x in range(1, 11): #the variable in the inner loop needs to be different to the one listed in the outer loop.
        print(x, end="") #this will print 1 to 10... and this end="" will print every iteration in the same line.
    print() #this will print a new line at the end of all the iteration.


#A little exercise for printing a rectangle:
rows = int(input("Please enter the number of rows you would like your rectangle to have: "))
columns = int(input("Please enter the number of columns you would like your rectangle to have: "))
symbol = input("Please enter the symbol you would like to use: ")

for x in range (rows):
    for y in range (0, columns):
        print(symbol, end="")
    print()