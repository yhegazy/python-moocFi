print("What is the weather forecast for tomorrow?")
temp=(int(input("Temperature: ")))
rain=(input("Will it rain (yes/no): "))
if temp > 20:
    print("Wear jeans and a T-shirt")

if  10 < temp <= 20:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")

if 5 < temp <= 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")

if temp <= 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!")