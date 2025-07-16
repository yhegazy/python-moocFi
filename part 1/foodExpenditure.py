# Write your solution here
timesAtCafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
typicalPrice = float(input("The price of a typical student lunch?"))
moneySpentOnGroceries = float(input("How much money do you spend on groceries in a week?"))



print("Average food expenditure:")
print(f"Daily: {((timesAtCafeteria * typicalPrice) + moneySpentOnGroceries) / 7} euros")
print(f"Weekly: {(timesAtCafeteria * typicalPrice) + moneySpentOnGroceries} euros")