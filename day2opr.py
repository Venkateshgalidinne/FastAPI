# Operators:
# perator is a symbol which is used to perform specific operations.

# types:
# 1. Arithmetic   → Mathematical operations
# 2. Comparison   → Compare values
# 3. Assignment   → Assign/update values
# 4. Logical      → Combine conditions
# 5. Identity     → Compare object identity (is , not is)
# 6. Membership   → Check whether a value exists (in ,not in)
# 

# Arithmetic operator:
# (+,-,*,/,//,%)
# print(10+22)
# print(199-299)
# print(9/2)
# print(566*622)
# print(9//2)
# print(9%2)

# Comparison operator:
# (<,>,<=,>=,==,!=)
# print(10>5)
# print(22<55)
# print(10<=10)
# print(20==20)
# print(55 != 500)

# Assigment operator:
# assigment operator is used to assign the variables.

# a =10
# a=a*10
# print(a)

# a = 9
# b=2
# c=a/b
# print(c)

# Logical operator:
# logocal operator is used to perform logical operators over the operands and we have 3types of operators

# And: when we need both oerands should me true then we need and operator.
# Or: when  we need either one of the operand is true then we need or operator.
# Not : will make results vice-versa.

# print(10 == 10 and 20 ==20)
# print(100 == 10 and 200 != 20)
# print("venkatesh"== "venkatesh" and 10==10)

# print("venkatesh" or 0)
# print(0 or "venkatesh")
# print(10 != 10 or 290 ==300)
# print(not 10==10 and 10 == 10)
# print(not 20==10 or 50 == 10)
# print(not "venkatesh" == "Venkatesh")
#
#  And Ex :
# percentage = 79
# known_python = True
# egliablity = percentage >= 65 and known_python
# print(egliablity)

# account_active = True
# balance =12000
# withdraw_amt =20000

# can_withdraw = account_active and balance >= withdraw_amt
# print(can_withdraw)

# age = 22
# percentage =75
# known_python = True

# print(age >= 18 and percentage >= 60)
# print(age >=25 or known_python)
# print(not known_python)

# Ternary operator:
#  it allows you to evalate a condition and return a value in single line code.
# syntax:
# value_if_true if condition else value_if_false

# age = 15

# status = "Eligable" if age >= 18 else"Not Eligable"
# print(status)


# marks = 22

# result = "pass " if marks >=36 else "Failed"
# print(result)

# number = 19
# result = "even" if number % 2==0 else "odd"
# print(result)