#To calculate compound interest

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount : "))
    if principle < 0:
        print("Principle cant be less than 0.")
    else:
        break
while True:
    rate = float(input("Enter the interest rate : "))
    if rate < 0:
        print("Interest rate cant be less than 0.")
    else:
        break
while True:
    time = int(input("Enter the time period (years) : "))
    if time < 0:
        print("Time period cant be less than zero.")
    else:
        break

total = principle * pow(( 1 + rate / 100), time)

print(f"Your Balance after {time} year/s is : ${total:.2f}")
