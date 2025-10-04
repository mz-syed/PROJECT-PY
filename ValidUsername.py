#Validate user input
#username must not be more than 12 characters long
#username must not contain any spaces
#username must not contain digits

username = input("Enter your username : ")

if len(username) > 12:
    print("Username can't be more than 12 characters long.")
elif username.count(" ") > 0:
    print("Username must not contain any spaces.")
elif not username.isalpha():
        print("Username must not contain any digits.")
else:
    print(f"Welcome {username}")