number = int(input("Enter number: "))

factorial = 1

for index in range(1, number + 1):
    factorial *= index

print(f"factorial of {number} is {factorial}")