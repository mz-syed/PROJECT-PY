#Python Calculator

operator = int(input("Enter the number for the operation you want to perform - 1. Addition  2. Subtraction  3. Multiplication  4. Division  5. Modulus: "))
a = float(input("Enter the first number you would like to calculate: "))
b = float(input("Enter the second number you would like to calculate: "))

if operator == 1:
    result = a + b
    print(f"a + b = {result}")
elif operator == 2:
    result = a- b
    print(f"a - b = {result}")
elif operator == 3:
    result = a * b
    print(f"a * b = {result}")
elif operator == 4:
    result = a / b
    print(f"a / b = {result}")
elif operator == 5:
    result = a % b
    print(f"a % b = {result}")
else:
    print("Invalid operator")
