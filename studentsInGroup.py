# Write your solution here
numberOfStudents = int(input("How many students on the course?"))
desiredGroupSize = int(input("Desired group size?"))

# Calculate the number of full groups
fullGroup = numberOfStudents // desiredGroupSize

# Check if there are remaining students that need an additional group
if numberOfStudents % desiredGroupSize != 0:
    fullGroup += 1

print(f"Number of groups formed: {fullGroup}")
