# The Fibonacci series is a sequence of numbers where each number is obtained by adding the previous two numbers.
# Fibonacci = Add the previous two numbers to get the next number.

num = int(input("Enter a Number :"))
a = 0
b = 1
for i in range(num):
    print(a, end = '')
    c = a+b
    a = b
    b = c