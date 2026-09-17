# what is Python ?
#  Python is a programming language #programming
#              interuppted language #line by line
#              dymically type language #a=10,  venkatesh ,[1,2,3] 
#              high level language #simple to understand english,math
#              beginner friendly language # everyone to built
#              large ecosystem based language #pandas,numpy,langchain,langgraph etc.
#              large community #Python knowns people    

# variables:
#  variable is container which holds the somedata.

# data: collection information

# rules of variables:
# can't start with numbers
# start with _  and letters[A,B,C][a,b,c]
# variable always a single name without any gaps b/w
# cannot be a python keyword.
# cannot contain spaces or special characters.
# can contain letters,digits and underscore.

# syntax:
# name = "Venkatesh"
# _age = 21

# types of variables:
# 1.local variable
# 2.Global variable
# 3.Instance variable

# 1.Local variable:
# a variable created inside a function is called a local variable.
# ex:
# def student_details():
#    name = "venkatesh" --local variable
#    age = 21 --local variable

#    print(name)
#    print(age)

# student_details()

# 2.Global Variables:
# a variable created outside a function is called a global variable.

# ex:
#  college =  "KKR&KSR Institute of Technology and sciences" # global variable

# def student_details():
#   print(college)

# student_details()
# print()

# 3.Instance Variable:
# an instance variable is belong to a praticular object.

# # ex: 
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# student1 = student("Venkatesh",22)
# student2 = student("Revanth",21)

# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)

# easy to  remember:
# Local → Function
# Global → Program
# Instance → Object


# Datatype:
# A datatype defines the kind of value that a variable can store in Python.
# types of data types 
# 1.single datatype or premitive datatype
# 2.Multi value datatype or non premitive datatype

# 1.single datatype or premitive datatype

# int      → Whole number
# float    → Decimal number
# str      → Text
# bool     → True / False

# ex:
# name = "venkatesh" --String
# age = 22  -- integer
# is_salary = 50000.20 ---float
# is_married = no --boolean

# 2.Multi value datatype or non premitive datatype

# list     → Multiple values, changeable
# tuple    → Multiple values, fixed
# set      → Unique values
# dict     → Key : Value

# ex:
# skills = ["Python","java","SQL"] -- list
# fruits = ("Apple","Banana","Mango")--tuple
# nums = {1,2,3,"pega","Python"}--set
# details = {"id":1,"name":venkatesh}--dict-- key value pairs

# index :
#  index number only string,tuple,list.
# index number start with positive zero(0) and aslo used negative number(-1)

# Accessing:
            # 0        1      2
# skills = ["Python","java","SQL"]
# # print(skills[1])
# print(skills[-3])


