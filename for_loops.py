# for loops = execute a block of code a fixed number of times.
#             we can itirate over a range, string, sequence, etc.

#let's count to 10.

for x in range (1 , 11):
    print(x)
print("Happy new year! ")

for x in reversed(range(1 , 11)):
    print(x)
print("Happy eastern!")

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)
print("Happy holidays!")
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)