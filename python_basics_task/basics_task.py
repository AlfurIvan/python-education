"""
There was a 1- tasks from python-basics file.
To save space and time, this file will contain simple subtasks that require up to 12 lines of code.
#  not a functions' coz of no logic :)
"""
#  from math import sqrt, sin, factorial  # import for task 13
import re                                 # import for task 14
import time, datetime, os, sys


print('\n1_____________________________\n')

#   subtask 1 -- print "Hello, World!" in console
"""Use the "print" function to print the line "Hello, World!"."""
print("Hello, World!")

print('\n2_____________________________\n')

#  subtask 2 shows the basic assignment of different types of variables
"""
The target of this exercise is to create a string, an integer, and a floating point number. The string should be 
named my_string_t2 and should contain the word "hello". The floating point number should be named my_float_t2 and 
should contain the number 10.0, and the integer should be named my_int_t2 and should contain the number 20.
"""
my_string_t2, my_float_t2, my_int_t2 = 'hello', 10.0, 20

if my_string_t2 == "hello":
    print("String: %s" % my_string_t2)
if isinstance(my_float_t2, float) and my_float_t2 == 10.0:
    print("Float: %f" % my_float_t2)
if isinstance(my_int_t2, int) and my_int_t2 == 20:
    print("Integer: %d" % my_int_t2)

print('\n3_____________________________\n')

#  subtask 3 shows basic operations with Lists
"""
In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. 
You must add the numbers 1,2, and 3 to the "numbers_t3" list, and the words 'hello' and 'world' to the strings_t3.
You will also have to fill in the variable second_name_t3 with the second name in the names_t3 list, using the brackets 
operator []. Note that the index is zero-based, so if you want to access the second item in the list, 
its index will be 1.
"""
numbers_t3, strings_t3 = [], []
names_t3 = ["John", "Eric", "Jessica"]

second_name_t3 = names_t3[1]

for i in range(3):
    numbers_t3.append(i + 1)

strings_t3.append('hello')
strings_t3.append('world')

print(numbers_t3, "\n", strings_t3, "\n", f"The second name on the names list is {second_name_t3}")

print('\n4_____________________________\n')

#  subtask 4
"""
The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the
 variables x and y, respectively. You are also required to create a list called big_list, which contains the variables 
 x and y, 10 times each, by concatenating the two lists you have created.
"""
x_t4 = object()
y_t4 = object()

x_list_t4 = [x_t4] * 10
y_list_t4 = [y_t4] * 10
big_list_t4 = x_list_t4 + y_list_t4

print(f"x_list contains {len(x_list_t4)} objects \n"
      f"y_list contains {len(y_list_t4)} objects \n"
      f"big_list contains {len(big_list_t4)} objects")
if x_list_t4.count(x_t4) == y_list_t4.count(y_t4) == big_list_t4.count(x_t4) == big_list_t4.count(y_t4) == 10:
    print("Almost there...\nGreat!")

print('\n5_____________________________\n')

#  subtask 5 about formatting strings
"""
You will need to write a format string which prints out the data using the following syntax: 
'Hello John Doe. Your current balance is $53.44.'
"""
data_t5 = ("John", "Doe", 53.44)
format_string_t5 = "Hello"

print("%s, %s %s. Your current balance is $%.2f." % (format_string_t5, data_t5[0], data_t5[1], data_t5[2]))
print(f"{format_string_t5}, {data_t5[0]} {data_t5[1]}. Your current balance is ${data_t5[2]}.")

print('\n6_____________________________\n')

#  subtask 6 about conditions
"""Hard work with strings and slices"""
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings, each containing only a word
print("Split the words of the string: %s" % s.split(" "))


print('\n7_____________________________\n')

#  subtask 7 about conditions
"""
Change the variables in the first section, so that each if statement resolves as True.
"""
number_t6 = 20
second_number_t6 = 0
first_array_t6 = [True, True, True]
second_array_t6 = [1, 2]

if number_t6 > 15 and first_array_t6 and (len(second_array_t6) == 2) \
        & (len(first_array_t6) + len(second_array_t6) == 5) \
        & (first_array_t6 and first_array_t6[0] == 1) & (not second_number_t6):
    for iterator_in_t6 in range(6):
        print(f"{iterator_in_t6 + 1}")

print('\n8_____________________________\n')

#  subtask 8 about Loops
"""
Loop through and print out all even numbers from the numbers list in the same order they are received. 
Don't print any numbers that come after 237 in the sequence.
"""
numbers_t7 = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865,
    575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
    953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
    24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440,
    380, 126, 721, 328, 753, 470, 743, 527
]

for number_t7 in numbers_t7:
    if number_t7 == 237:
        break

    if number_t7 % 2 == 1:
        continue
    print(number_t7)

print('\n9_____________________________\n')

#  subtask 9 about Functions
"""
Simply write the function's name followed by (), placing any required arguments within the brackets. 
For example, lets call the functions written above (in the previous example):
"""


def list_benefits_t8() -> [str]:
    """returns list of half's sentence"""
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]


def build_sentence_t8(benefit_t8) -> str:
    """:returns string"""
    return benefit_t8 + " is a benefit of functions!"


def name_the_benefits_of_functions_t8():
    """Function for concatenation body & odd"""
    list_of_benefits_t8 = list_benefits_t8()
    for benefit_t8 in list_of_benefits_t8:
        print(build_sentence_t8(benefit_t8))


name_the_benefits_of_functions_t8()

print("\n")

# sub subtask  about Multiple Function Arguments
"""
Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) The foo function must 
return the amount of extra arguments received. The bar must return True if the argument with the keyword magic_number is
 worth 7, and False otherwise.
"""


def foo_t9(a_t9, b_t9, c_t9, *args) -> int:
    return len(args)


def bar_t9(a_t9, b_t9, c_t9, **kwargs) -> int:
    return kwargs["magic_number_t9"] == 7


if foo_t9(1, 2, 3, 4) == 1:
    print("Good.")
if foo_t9(1, 2, 3, 4, 5) == 2:
    print("Better.")
if not bar_t9(1, 2, 3, magic_number_t9=6):
    print("Great.")
if bar_t9(1, 2, 3, magic_number_t9=7):
    print("Awesome!")

print('\n10_____________________________\n')

#  subtask 10 about Docstrings
"""
This is docstring. In docstrings contains a lot of useful information about modules, classes, functions.
Enjoy docstrings)
"""
print("Check code of this")


print('\n11_____________________________\n')

#  subtask 11 about Dictionaries
"""
Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
"""
phonebook_t11 = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}

phonebook_t11.pop("Jill")
phonebook_t11["Jake"] = 938273443
if "Jake" in phonebook_t11:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook_t11:
    print("Jill is not listed in the phonebook.")


print('\n12_____________________________\n')

#  subtask 12 about Sets
"""
In the exercise below, use the given lists to print out a set containing all the participants from event A which did 
not attend event B.
"""
a_t12, b_t12 = ["Jake", "John", "Eric"], ["John", "Jill"]

A_t12, B_t12 = set(a_t12), set(b_t12)

print(A_t12.difference(B_t12))


print('\n13_____________________________\n')

#  subtask 13 about Imports
#  I can use    import math     or      import math as m    for example
# But! better way to import smth is:
# from math import sqrt, sin, factorial ...  <---what do you need
print("Check the code))")


print('\n14_____________________________\n')

#  subtask 14 about Modules and Packages
"""
In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, 
which contain the word find.
"""
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

print('\n15_____________________________\n')

#  subtask 15 about Important python modules
"""
This task about couple of Important python modules: time, datetime, os and sys
I have read the documentation for them and give small useful examples of using each of them
"""
time.sleep(1)
print(datetime.date.today())
print(os.name)
print(sys.copyright)

print('\n16_____________________________\n')

#  subtask 16 about Files
"""
Here is simple work with file.
code below open text.txt, read them and close
"""
text_edu_file_t16 = open('text.txt', 'r')
line_from_file = [one_line.strip() for one_line in text_edu_file_t16]

print(line_from_file)
text_edu_file_t16.close()