story = input("Please type in a word: ")

while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    story += " " + word

print(story)