# Write your solution here
password = input("Password:")

while True:
    repeatPassword = input("Repeat password:")

    if password == repeatPassword:
        print("User account created!")
        break
    else:
        print("They do not match!")