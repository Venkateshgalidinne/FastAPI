# Error Handling Or Exception Handling:
# Exception handling is the process of detecting and handling errors that occur while a Python program is running, so the program can respond gracefully instead of crashing.
# Try
# except
# finally
# esle

# try:The try block contains the code that might cause an exception.
# try:
 
#    a =22
#    b = 2
#    print(a/b)

# Except:The except block handles the error if one occurs.
# try:
#     a = 10
#     b = 0

#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# # finally:finally is a block in exception handling that always executes, whether an exception occurs or not.
# try:
#     print(10 / 2)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# finally:
#     print("This always executes.")

#  else:The else block executes only when the try block completes successfully without any exception.

# try:
#     a = 10
#     b = 2

#     result = (a/b)
# except ZeroDivisionError:
#     print("cannot divsiable by 0")
# else:
#     print("Result:",result)
