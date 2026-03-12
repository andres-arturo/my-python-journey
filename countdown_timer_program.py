import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1): #this -1 will could backwards! :D
    print(x)
    time.sleep(1) #Esto "duerme" durante este tiempo


print(("Time's up!"))

my_time2 = int(input("Enter the time in seconds: "))
for x in range(my_time2, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time is up again! :D")
