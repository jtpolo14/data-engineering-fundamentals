# String variables
message1 = 'I LOVE DATA'
message2 = 'Python is cool'

# Integer variable
my_age = 25

# Float variable
pi_value = 3.14

# Boolean variable
is_learning = True

# Print all variables
print(message1)
print(message2)
print('Age:', my_age)
print('Pi value:', pi_value)
print('Learning Python:', is_learning)

# Check data types
print('Type of message1:', type(message1))
print('Type of my_age:', type(my_age))
print('Type of pi_value:', type(pi_value))
print('Type of is_learning:', type(is_learning))

# Converting data types (casting)
my_string = '12345'
print('Before conversion:', my_string, 'Type:', type(my_string))

my_integer = int(my_string)
print('After conversion:', my_integer, 'Type:', type(my_integer))

# More casting examples
number = 42
number_as_string = str(number)
print('Number as string:', number_as_string, 'Type:', type(number_as_string))

float_number = float(10)
print('Float from integer:', float_number, 'Type:', type(float_number))
