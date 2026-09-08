# for loops = execute a block of code a fixed number of times.
#             we can itirate over a range, string, sequence, etc.

#let's count to 10.

for x in range (1 , 11):
    print(x) #This will print from 1 to 10.
print("Happy new year! ")

for x in range (1, 11, 2): #This third number right here will count by the number you selected, for example, if you entered 2, will count 2 by 2.
    print(x) #will show 1, 3, 5, 7, 9 because it will start on 1, if we want 2, 4, 6, 8, 10, we need to start from 0.
print("2 by 2 :D")
for x in reversed(range(1 , 11)):
    print(x) #This will print from 10 to 1, literally reversed.
print("Happy eastern!")

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x) #This will print each character of credit_card, including the dashes (-).
print("Happy holidays!")
for x in range(1,21): #This part below will print 1 to 20 EXCEPT for the number 13.
    if x == 13:
        continue
    else:
        print(x)

for x in range(1,21): #This one is supposed to print from 1 to 20 BUUUUUT we used this time the "break" function, meaning that as soon as it reaches 13,
    # it will stop there, before 13.
    if x == 13:
        break #it will break on 12.
    else:
        print(x)