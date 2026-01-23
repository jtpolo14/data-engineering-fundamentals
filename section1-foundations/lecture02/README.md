# Lecture 02 - Variables and Data Types
--------------------
Description
-------------------- 
This lecture introduces variables and data types in Python. You will learn how to create variables, assign values to them, work with different data types, and convert between types.

By the end of this lecture, you will be able to:
* Create and assign values to variables
* Understand and use the four basic Python data types: strings, integers, floats, and booleans
* Use the `type()` function to check a variable's data type
* Convert between different data types using casting functions
* Store and manipulate different kinds of data in your programs
--------------------
Content
-------------------- 
Terminology
* Variable - a named location in memory used to store data that can be used and changed throughout a program
* Assignment - the action of giving a variable a value using the equals sign (=)
* Data Type - a particular kind of data item, as defined by the values it can take, the programming language used, or the operations that can be performed on it
* String - a sequence of text characters, enclosed in single ('') or double ("") quotes
* Integer - a whole number (not a fraction) that can be positive, negative, or zero (examples: 10, 0, -25, 5148)
* Float - a number with a decimal point (examples: 3.14, -0.5, 100.0)
* Boolean - a data type that can only be True or False
* Casting - setting or converting the data type of a variable
* Print - a Python function that displays output to the screen
* Syntax - the set of rules that defines how Python code must be written
--------------------
Lab
-------------------- 
Requirement(s)
* Create a program that demonstrates variables and different data types
* Create a new File
	* Open colab or text editor
	* Type the following code:
```python
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
```
* Run
```
I LOVE DATA
Python is cool
Age: 25
Pi value: 3.14
Learning Python: True
Type of message1: <class 'str'>
Type of my_age: <class 'int'>
Type of pi_value: <class 'float'>
Type of is_learning: <class 'bool'>
Before conversion: 12345 Type: <class 'str'>
After conversion: 12345 Type: <class 'int'>
Number as string: 42 Type: <class 'str'>
Float from integer: 10.0 Type: <class 'float'>
```
Understanding the code:
* Lines starting with # are comments - they help explain code but don't run
* The = sign assigns a value to a variable
* Strings use quotes, numbers don't need quotes, booleans are True or False (capitalized)
* The type() function tells you what data type a variable is
* int(), str(), float(), and bool() functions convert between data types
* Variable names can contain letters, numbers, and underscores but must start with a letter
--------------------
Help
-------------------- 
If you run into issues with the above lab, here are some helpful tips to try:
* Make sure the python version is 3.4 or above, lower versions and python 2 may not work
* Make sure the python file is saved with the '.py' file extension
* Make sure the vars_types.py file is saved inside the correct folder, in this example the folder name is mypi
* Be sure to type the terminal command exactly as shown, then press Enter
* Check that your quotes match - use either single ('') or double ("") quotes consistently
* Variable names are case-sensitive (Message1 is different from message1)
* Boolean values must be capitalized: True and False (not true or false)
* When converting strings to integers, the string must contain only numeric characters
Other resources:
* https://www.tutorialspoint.com/python3/python_variable_types.htm
* https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3
* https://www.w3schools.com/python/python_variables.asp
* https://realpython.com/python-data-types/
* https://www.programiz.com/python-programming/variables-datatypes
* https://en.wikipedia.org/wiki/Data_type
--------------------
What's next?
--------------------
* [Lecture 03 - Math]