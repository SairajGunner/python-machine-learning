input_list = input("Please enter a list of numbers separated by commas: \n")
input_list = input_list.split(",")
output_list = []

try:
    number_list = list(map(lambda x: int(x.strip()), input_list))
except ValueError:
    print("Seems like you did not enter only numbers.")
    exit()

for number in number_list:
    if (number % 2 == 0):
        output_list.append(number*number)

print(output_list)