input_number = input("Please input a number:\n")
prime = True
factor = 1

try:
    int(input_number)
except ValueError:
    print("Please enter a number")
    exit()

for index in range(2, int(input_number)):
    if (int(input_number) % index == 0):
        prime = False
        factor = index
        break

if (prime):
    print("{} is a prime number.".format(input_number))
else:
    print("{} is not a prime number. {} is one of its factors.".format(input_number, factor))