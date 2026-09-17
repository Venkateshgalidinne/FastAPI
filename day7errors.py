# Errors:
# An error is a problem in a program that prevents the program from behaving as expected.

# age = int(input("Enter your age: ")) 
# statement : invalid literal for int()

# Error Handling = Handling unexpected problems without crashing the entire program.

# types of errors:

# SyntaxError:A syntax error happens when Python's grammar/rules are incorrect.
# ex:
# if 10 > 5
#     print("yes")
# SyntaxError: expected ':'

# IndentationError:indentation as the spacing at the beginning of a line.

# Python uses indentation to understand which lines belong together.
# ex:
# if 22 > 9:
# print("yes")
# # IndentationError: expected an indented block after 'if' statement


# NameError:"I don't know what this name means."

# It usually happens when you use a variable, function, or object name that hasn't been defined.
# print(venkatesh)
# NameError: name 'venkatesh' is not defined

# TypeError:occurs when you perform an operation on a value of the wrong data type.
# Python expected one type, but you gave another type.
# ex:
# age = 22
# name = "Venkatesh"
# print(name + age)
# TypeError: can only concatenate str (not "int") to str

# ValueError:It occurs when the data type is correct, but the value is invalid for the operation.
# ex:
# age = int("Venkatesh")
# print(age)
# ValueError: invalid literal for int() with base 10: 'Venkatesh'

# KeyError: occurs when you try to access a dictionary using a key that does not exist.

# student = {
#     "name" : "venkatesh",
#     "age" : 22
# }

# # print(student["name"])
# print(student["course"])
# KeyError: 'course'

# AttributeError:The object exists, but the property or method you're asking for doesn't exist on that object.
# name = "venkatesh"
# print(name.age)
# AttributeError: 'str' object has no attribute 'age'

# ModuleNotFoundError:You told Python to import something, but Python cannot find it.
# import calucator
# ModuleNotFoundError: No module named 'calucator'

# RuntimeError:A runtime error occurs while your Python program is running.

# UnboundLocalError:Python knows the variable exists inside the function, but you are trying to use it before assigning a value.
# def student():
#     print(name)
#     name = "Venkatesh"

# student()
# nboundLocalError: cannot access local variable 'name' where it is not associated with a value.

# ZeroDivisionError:occurs when you try to divide a number by zero
# a= 10
# b=0
# c= a/b
# print(c)

# ZeroDivisionError: division by zero

# FileNotFoundError:occurs when Python tries to open or access a file that does not exist at the specified location.
# ex:
# file = open("user_data","r")
# FileNotFoundError: [Errno 2] No such file or directory: 'user_data'