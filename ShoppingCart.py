#Shopping Cart program

items = []
prices = []
total = 0

print("Welcome to our store!")
while True:
    item = input("Enter your item ( Press 'q' to quit ) : ")
    if item.lower() == "q":
        break
    else:
        price = float(input("Enter the price : $"))
        items.append(item)
        prices.append(price)

print()
print("= = = = = YOUR CART = = = = =")
for item in items:
    print(item)
print("= = = = = = = = = = = = = = =")
print()

while True:
    payment = input("Continue to check out? (Y / N) : ")
    if payment.lower() == "y":
        for price in prices:
            total += price
        print()
        print(f"Your total is ${total}")
        print("= = = THANK YOU FOR SHOPPING = = =")
        break
    elif payment.lower() == "n":
        print("Returning to shopping cart...")
        break










