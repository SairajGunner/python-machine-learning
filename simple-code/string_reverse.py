user_input = input()
reversed_string_array = list(range(0, len(user_input)))

for charIndex in range(0, len(user_input)):
    reversed_string_array[charIndex] = user_input[(len(user_input)-1) - charIndex]

print(''.join(reversed_string_array))