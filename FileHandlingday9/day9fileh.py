
# Read:
# file = open("student.txt","r")
# data = file.read()
# print(data)
# file.close()

# readline:
# file = open("student.txt","r")

# print(file.readline())
# print(file.readline())


# readlines:
# file = open("student.txt","r")

# data = file.readlines()
# print(data)

# print("hello\nworld")
# \n - new line

# w — Write Mode:

# file = open("student.txt","w")
# file.write("Vamsi")

# # a — Append Mode:
# file = open("student.txt","a")
# file.write("\nPraveen")
# file.write("\nChatinaya")

# x-create mode:

# file = open("newfile.txt","x")

# file = open("newfile.txt","w")
# file = open("newfile.txt","a")
# file.write("Hello Venkatesh")
# file.write("Are u interst to join the GenAi course")

# Writing Multiple Lines
# students = [
#     "Venkatesh\n",
#     "Vamsi\n",
#     "Sumanth\n"
# ]

# with open("student.txt","w")as  file:
#   file.writelines(students)


# name = input("Entre student name :")
# marks = input("Entre the Marks:")
# subject = input("Entre subject Name :")

# with open ("student.txt","a")as file:
#     file.write(name +"," + marks + "," + subject + "\n")

# with open("student.txt","r") as file:

#     for students in file:
#         print(students.strip())

# file = open("user.txt","x")
# students = [
#     "Venkatesh\n",
#     "Vamsi\n",
#     "Sumanth\n"
# ]

# with open("user.txt","w")as file:
#   file.writelines(students)

# username = input("Entre the User Name :")

# with open ("user.txt","r") as file:

#     user = file.read().splitlines()

# if username in user:
#     print("Login sucessfully")
# else:
#     print("user not found")

# with open("user.txt","a") as file:
 
#  file.write("Manago\n")
#  file.write("Watermelon\n")
# # file.close()

# with open("user.txt","r") as file:
#  data = file.read()
#  print(data)

# with open ("fruits.txt","a") as file:
#     file.write("Grapes\n")
#     file.write("Dates\n")

# with open ("fruits.txt","r") as file:
#     data = file.read()
#     print(data)

# items = input("Enter the Name:")
# quantity = input("Entre the quantity:")

# with open("order.txt","a")as file:
#     file.write (items + " - " + quantity +"\n")
#     print("order saved")
 
# Transaction = input("Entre Transcation:")
# with open ("transcation.txt","a") as file:
#     file.write(Transaction +"-" "\n")
#     # print("Transacation is sucess")

# name = input("Enter student Name :")
# age = input("Enter student Age:")
# course = input("Entre Course:")
# with open("student.txt","a") as file:
#     file.write(name + "," +age +"," +course + "\n")
#     print("Student Registration Sucessfully")


# Name = input("Enter Employee Name :")
# Id = input("Enter Employee ID :")
# Department = input("Enter Employee Department :")
# Salary = input("Enter the Employee Salary:")
# with open ("Emoplyee.txt","a")as file:
#     file.write(Name + "," + Id + "," + Department + "," + Salary + "\n")