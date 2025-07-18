limit = int(input("Limit: "))
sum = 0
number = 1
calculation = "The consecutive sum: "

while sum < limit:
    sum += number
    # Add the number to the calculation string
    calculation += str(number)
    if sum < limit:
        calculation += " + "
    number += 1

calculation += f" = {sum}"
print(calculation)