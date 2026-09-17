# Polymorphism :
# poly = Many
# morphism = Fotms
# In Python, the same method, function, or operator can behave differently depending on the object or data being used.

# Same method
#     ↓
# Different objects
#     ↓
# Different behavior

# Types of polymorphism:
# 1.Method Overriding
# 2.Method Overloading
# 3.Operator Overloading
# 4.Duck Typing

#  1.Method Overriding:
# Method overriding occurs when a child class provides its own implementation of a method that is already defined in the parent class.
#          Parent Class
#         work()
#            ↓
#     ┌──────┴──────┐
#     ↓             ↓
#  Developer       Tester
#  work()          work()

# class Manager:
#     name = "Venkatesh"

#     def __init__(self,name,role,exp,salary):
#         self.name = name
#         self.role = role
#         self.exp = exp
#         self.salary = salary

#     def Mr_details(self):
#         print("Name:",self.name)
#         print("ROle:",self.role)
#         print("EXP:",self.exp)
#         print("Package:",self.salary)

# class Sr_Manager(Manager):
#     name = "Hitesh"
#     def __init__(self,name,role,exp,salary):
#         self.name = name
#         self.role = role
#         self.exp = exp
#         self.salary = salary

#     def sr_details(self):
#         print("Name:",self.name)
#         print("ROle:",self.role)
#         print("EXP:",self.exp)
#         print("Package:",self.salary)

# class Jr_Manager(Manager):
#     name = "Leela"
#     def __init__(self,name,role,exp,salary):
#             self.name = name
#             self.role = role
#             self.exp = exp
#             self.salary = salary
    
#     def jr_details(self):
#             print("Name:",self.name)
#             print("ROle:",self.role)
#             print("EXP:",self.exp)
#             print("Package:",self.salary)


# M = Jr_Manager("Leela",
#                "Jr.Manager",
#                4,
#                "7LPA"
# )

# M1 = Sr_Manager("Hitesh",
#      "Sr.manager",
#      10,
#      "12LPA"
# )

# M2 = Manager("Venkatesh","Manager",15,"22LPA")

# M2.Mr_details()
# print("--------------")
# M1.sr_details()
# print("--------------")
# M.jr_details()

# class Payment:

#     def pay(self,amount):
#         print("Processing the Payment")

# class UPI(Payment):
#     def pay_UPI(self,amount):
#         print("Paid ₹",amount,"Using UPI")

# class Creditcard(Payment):
#     def pay_Credit(self,amount):
#         print("Paid ₹",amount,"using CreditCard")

# class Cash(Payment):
#     def pay_cash(self,amount):
#         print("Piad ₹",amount,"Pay on cash")

# upi = UPI()
# Credit = Creditcard()
# cash = Cash()

# upi.pay_UPI(10000)
# Credit.pay_Credit(25000)
# cash.pay_cash(80000)
        
# 2.Method overloading:
# Method overloading means using the same method name to perform different operations depending on the number or type of arguments passed to it.

# class Calculator:

#     def add(self,a,b=0):
#         return a+b

#     def sub(self,a,b=0):
#         return a-b

# c = Calculator()

# print(c.add(10,99))
# print(c.sub(1299,1598))


    