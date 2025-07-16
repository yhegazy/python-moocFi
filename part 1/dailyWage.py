# Write your solution here
hourly = float(input("Hourly wage:"))
hoursWorked = int(input("Hours worked:"))
dayOfWeek = input("Day of the week:")

if dayOfWeek == "Sunday":
    hourly *= 2

print(f"Daily wages: {hourly * hoursWorked} euros")    
