# Save the input in this variable
ticket = input()

# assign each element in the string entered to a var
first_str = ticket[0]
second_str = ticket[1]
third_str = ticket[2]
fourth_str = ticket[3]
fifth_str = ticket[4]
sixth_str = ticket[5]

# convert the var type from str to int
first_digit = int(first_str)
second_digit = int(second_str)
digit_three = int(third_str)
fourth_digit = int(fourth_str)
fifth_digit = int(fifth_str)
sixth_digit = int(sixth_str)

# Add up the digits for each half
half1 = first_digit + second_digit + digit_three
half2 = fourth_digit + fifth_digit + sixth_digit

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
