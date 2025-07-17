from math import sqrt
# Write your solution here
while True:
    number = int(input("Please type a number:"))

    if number < 0:
        print("Invalid number")
    elif number == 0:
        print("Exiting...")
        break;
    else:
        print(f"{sqrt(float(number))}")