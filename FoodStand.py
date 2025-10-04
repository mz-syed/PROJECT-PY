#Concession stand

menu = {"Hotdog" : 5.99, "Fries" : 2.50, "Burger" : 6.00, "Nachos" : 3.40, "M&Ms" : 1.99,
        "Coke" : 1.50, "Sprite" : 1.50, "Popcorn" : 99.99}
cart = []
total = 0

print("======MENU=======")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("=================")

while True:
     food = input("Enter the name of item you what to purchase ( 'Q' to exit ): ").capitalize()
     if food == "Q":
         break
     elif menu.get(food) is not None:
         cart.append(food)
         total += menu.get(food)
     elif menu.get(food) is None and food != "q":
         print("Item is not on the menu.")

print()
print("=== YOUR ORDER ===")
for item in cart:
    print(item, end = ", ")
print()
print(f"Your total is : ${total:.2f}")
print("=================")

