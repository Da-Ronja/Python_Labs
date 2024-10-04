"""
1.
Understand what a lambda function is and when to use it in Python.
"""
# 1.a) Research and explain what a lambda function is.
"""
A lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression. 
Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Lambda functions are often used as arguments to higher-order functions or for creating short, throwaway functions.
"""
# Code Example:
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# 1.b) Describe situations where using a lambda function would be more appropriate than defining a full function using def.
"""
Lambda functions are used when you need a small function for a short period of time. They are used in situations where you need a function for a short period of time and you don't want to define a full function using def.
Example:
    - When you want to sort a list of tuples based on the second element of the tuple.
    - When you want to filter a list based on a condition.
    - When you want to map a function to a list.
"""
# Code Examples:
# Sorting a list of tuples by the second element
tuples_list = [(1, 3), (2, 2), (3, 1)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)  # Output: [(3, 1), (2, 2), (1, 3)]

# Filtering a list to keep only even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Mapping a function to double the values in a list
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10, 12]

# 1.c) Explain the following terms in relation to lambda:
"""
1.c.1) Anonymous function
    An anonymous function is a function that is defined without a name. While normal functions are defined using the def keyword, anonymous functions are defined using the lambda keyword. 
    Lambda functions are used when you need a small function for a short period of time.
1.c.1) Inline function
    An inline function is a function that is defined in a single line of code. Lambda functions are inline functions because they are defined in a single line of code.
"""
# Code Example:
# Here’s a demonstration of an anonymous function:
anonymous_function = lambda x: x ** 2
print(anonymous_function(4))  # Output: 16

# Inline function example:
inline_example = lambda x, y: x * y + 1
print(inline_example(2, 3))  # Output: 7

"""
2.
Understand how to use filter() in Python with a lambda function to select elements from a list that meet a certain condition.
"""
# 2.a) Explain what filter () does in Python and what kind of result it returns.
"""
The filter() function in Python is used to filter out elements from a list based on a certain condition. It takes a function and a list as arguments and returns an iterator containing the elements for which the function returns True.
"""

# 2.b) Create an example scenario where you need to filter out elements from a list.
"""
Example:
You are given a list of numbers, and you need to keep only the even numbers. How would you approach this using filter ()?
"""
# Code Example:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]

"""
3.
Learn how to use map() to apply a transformation to every item in a list.
"""

# 3.a) Explain the purpose of map() and how it works in Python.
"""
The map() function in Python is used to apply a function to every item in a list or iterable and return a new list with the results. It takes a function and a list (or other iterable) as arguments and applies the function to each item in the list.
"""

# 3.b) Create a real-life scenario where you need to modify every element of a list in the same way.
"""
Example:
You have a list of prices, and you want to apply a 10% discount to each. How would you use map () with a lambda function to achieve this?
Step 1: Define the list of prices.
Step 2: Use the map() function with a lambda function to apply the discount to each price.
Step 3: Convert the result to a list and print it. 
"""
# Code Example:
prices = [100, 200, 300, 400, 500]
discounted_prices = list(map(lambda x: x * 0.9, prices))

print(discounted_prices)  # Output: [90.0, 180.0, 270.0, 360.0, 450.0]

"""
4.
Learn how to combine the functionality of  filter() and map() to both select and modify elements in a list.
"""

# 4.a) Describe a scenario where you need to filter out unwanted elements from a list and then modify the remaining elements.
"""
Scenario:
You have a list of strings, and you want to filter out strings with fewer than 5 characters and then convert the remaining strings to uppercase.
"""
# Code Example:
# Scenario:
strings = ["apple", "banana", "kiwi", "orange", "grape"]
filtered_strings = list(filter(lambda x: len(x) >= 5, strings))
uppercased_strings = list(map(lambda x: x.upper(), filtered_strings))

print(uppercased_strings)  # Output: ['BANANA', 'ORANGE']

# 4.b) Break down the process of applying filter () first, and then using map() on the filtered result.
"""
Step 1: Use filter() to filter out unwanted elements from the list.
Step 2: Use map() to apply a transformation to the filtered elements.
Step 3: Convert the result to a list and print it.
"""


"""
5.
Understand Python's scope rules and how they affect variable lookup and access in different contexts.
"""

# 5.a) Explain the LEGB rule: Local, Enclosing, Global, Built-in.
"""
The LEGB rule is the order in which Python looks for variable names in different scopes. It stands for: Local, Enclosing, Global, Built-in.
    - Local: Variables defined within a function.
    - Enclosing: Variables defined in the enclosing function.
    - Global: Variables defined in the global scope.
    - Built-in: Python's built-in functions and keywords.
"""

# Code Example demonstrating the LEGB rule:
x = "Global x" # Global variable

def outer_function():
    x = "Enclosing x" # Enclosing variable
    
    def inner_function():
        x = "Local x" # Local variable
        print("Inner Function x:", x) # Outputs Local x
        
    inner_function()
    print("Outer Function x:", x) # Outputs Enclosing x

outer_function()
print("Global x:", x) # Outputs Global x

# 5.b) Describe what happens to a variable when it is defined:
"""
5.b.1) Inside a function (local):
    When a variable is defined inside a function, it is considered a local variable and is only accessible within that function.
5.b.2) Inside a function within another function (enclosing):
    When a variable is defined inside a function within another function, it is considered an enclosing variable and is accessible within the inner function and any enclosing functions.
5.b.3) In the main body of the program (global):
    When a variable is defined in the main body of the program, it is considered a global variable and is accessible throughout the program.
5.b.4) As a built-in function (built-in):
    Built-in functions are predefined functions in Python that are always available for use. They are part of the Python standard library and do not need to be imported.
"""

# Example:
"""
Imagine you have a variable called x that exists in the global scope and is also redefined inside a function. 
Explain how Python resolves which value of x to use at different points in the program.
"""
"""
Explaination:
When a variable x is referenced within a function, Python first looks for a local variable x within the function.
If there is no local variable x, Python then looks for an enclosing variable x in the enclosing function.
If there is no enclosing variable x, Python then looks for a global variable x in the global scope.
If there is no global variable x, Python then looks for a built-in variable x in the built-in functions.
The variable x used in the function will be resolved based on this order of lookup (LEGB rule).
"""
x = 10  # Global variable

def my_function():
    x = 20  # Local variable
    print(x)  # Output: 20

my_function()
print(x)  # Output: 10
