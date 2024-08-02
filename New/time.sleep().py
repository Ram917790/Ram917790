import time

my_time=int(input("enter a time in seconds : "))

for x in range(my_time,0,-1):
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    time.sleep(1)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
     #this will sleep for 1 second in each iteration of loop

print("Time up")
