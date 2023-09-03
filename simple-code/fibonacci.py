input_number = input("Please enter a number\n")
output = 1

try:
    int(input_number)
except ValueError:
    print("Please input a number.")
    exit()

for index in range(1, int(input_number) + 1):
    output *= index

print(output)
