# Write your solution here
number = int(input("Number:"))

if number % 15 == 0:  
    print("FizzBuzz")
elif number % 5 == 0:  
    print("Buzz")
elif number % 3 == 0: 
    print("Fizz")
else:
    print(number)  