# Question 1
# user_int_1 = int(input())
# user_int_2 = int(input())
# user_int_3 = int(input())

# site_a = 15.62
# site_b = 41.85
# site_c = 32.67

# total = 0

# site_a_total = site_a * user_int_1
# site_b_total = site_b * user_int_2
# site_c_total = site_c * user_int_3

# total = site_a_total + site_b_total + site_c_total

# print(f"Distance: {total:.2f} miles")


# Question 2
# Create a solution that accepts an integer input representing any number of ounces. Output the converted total 
# number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds 
# in a ton.

# user_input = int(input())

# tons = user_input // 32000
# pounds = (user_input % 32000) // 16
# ounces = (user_input % 32000) % 16

# print(f"Tons: {tons}") 
# print(f"Pounds: {pounds}")
# print(f"Ounces: {ounces}")

# Question 3

# Create a solution that accepts an integer input representing the index value for any any of the five elements in the following list:
# various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
# Using the built-in function type() and getting its name by using the .name attribute, output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.

# various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

# user_input = int(input())

# if user_input < len(various_data_types):
#     result = type(various_data_types[user_input]).__name__
#     print(f"Element {user_input}: {result}")
# else:
#     print("Error")

# Question 4

# Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a 
# trapezoid in meters. Output the exact area of the trapezoid in square meters as a float value. The exact area of a trapezoid 
# can be calculated by finding the average of the two base measurements, then multiplying by the height measurement.

# Trapezoid Area Formula:
# A = [(b1 + b2) / 2] * h

# b1 = int(input())
# b2 = int(input())
# height = int(input())

# area = ((b1 + b2) / 2) * height

# print(f"Trapezoid area: {area:.1f} square meters")

# Question 5

# Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to 
# the requested data type prior to finding the sum.

# First output: sum of five inputs maintained as integer values
# Second output: sum of five inputs converted to float values
# Third output: sum of five inputs converted to string values (concatenate)

# user_int_1 = int(input())
# user_int_2 = int(input())
# user_int_3 = int(input())
# user_int_4 = int(input())
# user_int_5 = int(input())

# total = user_int_1 + user_int_2 + user_int_3 + user_int_4 + user_int_5
# total_str = str(user_int_1) + str(user_int_2) + str(user_int_3) + str(user_int_4) + str(user_int_5)

# print(f"Integer: {total}")
# print(f"Float: {float(total)}")
# print(f"String: {str(total_str)}")

# Question 6

# Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. 
# Output the identification number as a string with no spaces.
# The solution output should be in the format
# 111-22-3333

# user_input = int(input())

# first = user_input // 1000000
# second = (user_input % 1000000) // 10000
# third = (user_input % 10000)

# print(f"{first}-{second}-{third}")

# Question 7

# Create a solution that accepts an integer input to compare against the following list:

# predef_list = [4, -27, 15, 33, -10]
# Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list
# The solution output should be in the format

# predef_list = [4, -27, 15, 33, -10]

# user_input = int(input())

# if user_input > max(predef_list):
#     result = True
#     print(f"Greater Than Max? {result}")
# else:
#     result = False
#     print(f"Greater Than Max? {result}")


# Question 8

# Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. Output a description of 
# the water state based on the following scale:

# If the temperature is below 33° F, the water is “Frozen”.
# If the water is between 33° F and 80° F (including 33), the water is “Cold”.
# If the water is between 80° F and 115° F (including 80), the water is "Warm".
# If the water is between 115° F and 211° (including 115) F, the water is “Hot".
# If the water is greater than or equal to 212° F, the water is “Boiling”.
# Additionally, output a safety comment only during the following circumstances:

# If the water is exactly 212° F, the safety comment is "Caution: Hot!"
# If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"

# user_input = int(input())

# if user_input < 33:
#     print("Frozen")
#     print("Watch out for ice!")
# elif user_input >= 33 and user_input <= 80:
#     print("Cold")
# elif user_input >= 80 and user_input <= 115:
#     print("Warm")
# elif user_input >= 115 and user_input <= 211:
#     print("Hot")
# elif user_input >= 212:
#     print("Boiling")
#     print("Caution: Hot!")


# Question 9
# frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# try:
#     user_input = int(input())
#     if 0 <= user_input < len(frameworks):
#         print(frameworks[user_input])
#     else:
#         print("Error")   
    
# except IndexError:


#     print("Error")
# Question 10
# def calculate_total_price(num_shares, stock_selections):
#     stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

#     total_price = 0

#     for i in range(num_shares):
#         stock_symbol = stock_selections[i].upper()  # Convert stock symbol to uppercase for case-insensitivity
#         if stock_symbol in stocks:
#             total_price += stocks[stock_symbol]
#         else:
#             print(f"Error: Stock '{stock_symbol}' not found.")

#     return total_price


# # Input
# num_shares = int(input())
# stock_selections = [input() for _ in range(num_shares)]

# # Calculate total price
# total_price = calculate_total_price(num_shares, stock_selections)

# # Output
# print(f"Total price: ${total_price:.2f}")


# Question 11
# purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

# total = 0

# user_str = input("enter item: ")
# user_int = int(input("enter quantity: "))

# if user_str in purchase:
#     if user_int < 10:
#         total += purchase[user_str] * user_int # no discount
#     elif user_int >= 10 and user_int <= 20:
#         total += purchase[user_str] * user_int * 0.95 # 5% discount
#     elif user_int > 21:
#         total += purchase[user_str] * user_int * 0.9 # 10% discount
#     else:
#         print("error")
# else:
#     print("error")


# print(f"{user_str} ${total:.2f}")

# Question 12
# Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt". 
# Each text file contains three rows with one word per row. 
# Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string 
# composed of the three existing words to the end of the file contents on a new line. Output the new file contents.

# with open("WordTextFile1.txt", "r+") as f:
#     f.write("cat\n")
#     f.write("chases\n")
#     f.write("dog\n")
#     f.write("cat chases dog")

    
#     print(f.read())


# Question 13
# Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". 
# Each file contains two rows of comma-separated values. Import the built-in module csv and use its open() function and reader() 
# method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. 
# Output the file contents as two dictionaries.

# import csv

# try:
#     with open("input1.csv", "r", newline='') as f:
#         reader = csv.reader(f)
#         # Assuming there are two rows in the CSV file
#         row1 = next(reader)
#         row2 = next(reader)

#         # Create dictionary 
#         dict1 = {f"key{i+1}": value for i, value in enumerate(row1)}
#         dict2 = {f"key{i+1}": value for i, value in enumerate(row2)}
#         # Output
#         print(dict1)
#         print(dict2)
# except FileNotFoundError:
#     print("Error: File not found.")
# except Exception as e:
#     print(f"Error: {e}")


# Question 14

# Create a solution that accepts an integer input. Import the built-in module math and use its factorial() method to 
# calculate the factorial of the integer input. Output the value of the factorial, as well as a Boolean value identifying 
# whether the factorial output is greater than 100.

# import math

# user_input = int(input())

# factorial = math.factorial(user_input)
# if factorial > 100:
#     print(factorial)
#     print(True)
# else:
#     print(factorial)
#     print(False)


# # print(factorial)

# Question 15

# Create a solution that accepts an integer input representing the age of a pig. 
# Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent 
# age of a pig. A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.

# import pigAge

# pigAge_converter = pigAge.pigAge_converter

# user_input = int(input())

# result = pigAge_converter(user_input)

# print(f"{user_input} is {result} in human years")



