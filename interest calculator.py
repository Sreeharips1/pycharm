principle=0
rate=0
time=0
while principle <=0:
    principle=float(input("Enter the principle: "))
    if principle <=0:
        print("Please enter a positive value")
while rate <=0:
    rate=float(input("Enter the rate: "))
    if rate <=0:
        print("Please enter a positive value")
while time <=0:
    time=int(input("Enter the time: "))
    if time <=0:
        print("Please enter a time value")
9
total= principle*pow((1+rate/100),time)
print(f"the total value is {total}")
