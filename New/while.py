principle=float(input("Enter a principle"))
time = float(input("time"))
rate = float(input("rate"))

while principle <=0:
    principle=float(input("Enter a principle"))
    if principle <=0:
        print("It should not be 0")
        

while time <=0:
    time=float(input("Enter a time"))
    if time <=0:
        print("Time should not be 0 or negative")

while rate <=0:
    rate=float(input("Enter a rate"))
    if rate <=0:
        print("Rate should not be 0 or negative")
        

total = principle * (1 + rate/100) ** time - principle
print(f'The principle is {principle} and rate is {rate} times is {time} the Total is {total}')