# Conditional Statements
#  A conditional statement is used to make decision in a python program based on a condition.
# Type of conditonal statements:
# 1.if
# 2.If else
# 3.If elif else
# 4.Nested If

# 1.If statement:
# the if statement execute code only the condition is True.

# syntax:
# if condition:
#     statement

# # ex:

# age= 15
# if age>=18:
#  print("you are eligable for vote")

# amt = 90000

# if amt >= 10000:
#     print("sufficent amt for transction")

# # If else statement:
# sometimes we need two possible outcomes[True/False]

# marks = int(input("Enter the Marks :  "))

# if marks >=50:
#     print("Pass")
# else:
#     print("Failed")

# username = "venkatesh"
# password = "2200"

# if username == "venkatesh" and password == "2209":
#     print("Login sucessfully")
# else:
#     print("Invalid username or password")

# min_bal = "1000"
# password = "2209"

# if min_bal >= "3000" and password == "2209":
#     print("Minimun amount is there")
# else:
#     print("Insufficient amount")

# if-elif-else:
# what if there are more two possibillites.

# syntax:
# if condition1:
#     statement
# elif condition2:
#     statement
# elif condition3:
#     statement
# else:
#     statement

# units = int(input("Enter the Number of Units:"))

# if units <=100:
#     print("low usage")
# elif units <=250:
#     print("Medium usage")
# elif units <=350:
#     print("Normal usage")
# elif units <= 450:
#     print("High usage")
# else:
#     print("Alert very high usage")


# marks = int(input("Enter the marks:.."))

# if marks >=96:
#     print("A Grade")
# elif marks >=85 and marks <=95:
#     print("B+ Grade")
# elif marks >=71 and marks <=84:
#     print("B Grade")
# elif marks >=61 and marks <=70:
#     print("C Grade")
# elif marks >=50 and marks <=60:
#     print("D Grade")
# elif marks >=36 and marks <=49:
#     print("E Grade")
# else:
#     print("Failed")


# age = int(input("Enter the age:"))

# if age <= 5:
#     price = 0
# elif age <= 12:
#     price = 100
# elif age <= 18:
#     price = 150
# else :
#     price = 200

# print("Ticket price:",price)


# amount = int(input("Enter the amount:"))

# if amount >= 10000:
#     Discount = 20
# elif amount >= 5000:
#     Discount = 10
# elif amount >= 2000:
#     Discount = 5
# else:
#     Discount = 0

# print("Discount:",Discount,"%")


# amount = int(input("Enter the amount:"))

# if amount >= 10000:
#     discount = 20
# elif amount >= 5000:
#     discount = 10
# elif amount >= 2000:
#     discount = 5
# else:
#     discount = 0

# discount_amount = amount * discount / 100
# final_amount = amount - discount_amount

# print("original amount:",amount)
# print("Discount:",discount_amount)
# print("Final amount:",final_amount)


# balance = 25000
# print("balance:",balance)
# withdraw = int(input("Enter the Amount:"))

# if withdraw <= 0:
#     print("Invalid amount")
# elif withdraw > balance:
#     print("Insuffcient amount")
# else:
#     balance = balance - withdraw
#     print("withdraw successfull")
#     print("remaining balance:",balance) 

# units = int(input("Enter the Number of Units:"))

# if units <= 100:
#     Bill = units * 2
# elif units <= 101 and units >= 200:
#     Bill = units * 3
# elif units <= 201 and units >= 300:
#     Bill = units * 5
# else:
#     Bill = units * 7

# print("Electricity bill:",Bill)


# number = int(input("Enter the Number:"))

# if number % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")
 
# Nested IF :
# A nested if means writing one if statement inside another if statement.

# syntax:
# if condition1:
#     if condition2:
#         # code
#     else:
#         # code
# else:

# username = input("Enter the username :")
# password = input("Enter the Password:")

# if username == "Venkatesh":

#    if password == "2209":
#       print("Login Successfull")
#    else:
#       print("Incorrect Password")

# else:
#    print("Incorrect username")

# age =int(input("Enter the age: "))
# balance = 5000
# print("Balance:",balance)
# withdraw = int(input("Enter the amount :"))

# if age >= 18:
#     print("You are Eligible")

#     if withdraw <= balance:
#        print("Withdraw successfully")
#        balance = balance - withdraw 
#        print("Remaining Balance :",balance)
#     else:
#       print("Insufficient Balance")
# else:
#   print("You are Not Eligible")

age = int(input("Enter the age:"))
has_id = True

if age >=18:

    if has_id :
        print("Entry allowed")
    else:
        print("ID required")

else:
    print("Not Eligible")
  