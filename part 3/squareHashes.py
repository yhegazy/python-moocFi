# Write your solution here
# You can test your function by calling it within the following block
def hash_square(value):
    index = 0

    while index < value:
        print("#" * value)
        index +=1


if __name__ == "__main__":
    hash_square(5)