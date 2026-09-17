# oops : object oriented programming language 
# oops is divided into 2 phases

# oops phase-1:
# class
# object
# self
# __init__
# instance
# class variable
# instance variable
# local variable
# instance method

# class:

# class student:
#     name = "Venkatesh"
#     age = "22"
#     course = "Geni AI"

# obj = student()
# print("Name :",obj.name)
# print("Age:",obj.age)
# print("Course:",obj.course)

# Student → Class
# obj → Object
# name, age, course → Attributes
# obj.name → Accessing an attribute through the object

# Class with __init__():

# class Vegetables:

#     def __init__(self):

#         self.vegname = "carrot"
#         self.Quanity = "1KG"
#         self.price = "60"
#         self.Hybrid = "Yes"

# obj = Vegetables()
# print("Vegetable Name :",obj.vegname)
# print("Quanity:",obj.Quanity)
# print("Cost:",obj.price)
# print("Hybrid:",obj.Hybrid)

# class Fruits:

#     def __init__(self,name,Quanity,Price):
#         self.name = name
#         self.Quanity = Quanity
#         self.Price = Price

#     def display(self):
#         print("Fruit Name:",self.name)
#         print("Quanity:",self.Quanity)
#         print("Price:",self.Price)

#     # def total_Price(self):
#     #     return self.Price * self.Quanity

# Fruits1 = Fruits("Banana","1danjana","80")
# Fruits2 = Fruits("Mango","1KG","150")
# Fruits3 = Fruits("Grapes","1KG","120")


# Fruits1.display()
# print()
# Fruits2.display()
# print()
# Fruits3.display()

# print("Total Price:",Fruits1.total_Price())
# print("Total Price:",Fruits2.total_Price())
# print("Total Price:",Fruits3.total_Price())

# class Foodorder:
#     def __init__(self,Customer,Food,Price ,Quanity):
#         self.Customer = Customer1
#         self.Food = Food
#         self.price = Price
#         self.Quanity = Quanity

#     def bill(self):
#         Total = self.price * self.Quanity

#         print("Customer:",self.Customer)
#         print("Food:",self.Food)
#         print("Price:",self.price)
#         print("Quanity:",self.Quanity)
#         print("Total Bill:",Total)

# order1 = Foodorder("Venkatesh", "Biriyani", 299, 3)
# order2 = Foodorder("Ganesh", "Large Mandi", 1499, 2)
# order3 =Foodorder("Srilakshmi", "Meals", 199, 5)

# order1.bill()
# print()
# order2.bill()
# print()
# order3.bill()


# class Patient:

#     def __init__(self,name,age,disease):
#         self.name = name
#         self.age = age
#         self.disease = disease

#     def display(self):
#         print("Patient Name:",self.name)
#         print("Age:",self.age)
#         print("Patient Disease:",self.disease)

# Patient1 = Patient("Venkatesh", "22","Fever")
# Patient2 = Patient("Sai","25","Cold & Coaf")

# Patient1.display()
# print()
# Patient2.display()

# class Car:
#     def __init__(self,Brand,Model,Price):
#         self.Brand = Brand
#         self.Model = Model
#         self.Price = Price

#     def start(self):
#         print(self.Brand, "Car is started")

#     def display(self):
#         print("Brand:",self.Brand)
#         print("Model:",self.Model)
#         print("Price:",self.Price)

# car1 = Car("Audio","X6","40000000")
# car2 = Car("Mahindra","Thar","2000000")

# car1.display()
# print()
# car2.display()


# class Institute :

#     name = "venkatesh"
#     location = "Kondapur,Hyderbad"

#     def __init__():
#         a = 10
#         print("Default method")
#     def Trainer():
#         allTrainers = ["venkatesh","Revanth","Teja"]
#         print(allTrainers)

#     def Management():
#         allmanagement = ["Hitesh","Krishna","sai"]
#         print(allmanagement)

# obj = Institute()


# obj.__init__()
# obj.Trainer()
# obj.Management()


# batchName = "Gen-1"
# totalstudents = 20

# def btachstartdate():
#     date = "01-08-2026"
#     print("Date:",date)

# class Institute:
#     name = "10000coders"
#     loc = "KPHB Road number -3 "

#     def __init__(self):
#         a = 10
#         self.course = "Generative AI & Agentic AI"
#         self.fee    = "30000"
#         # print("init default method")

#     def Trainers(self):
#         self.allTrainers = ("Venkatesh","Revanth","Hitesh")
#         self.cricketer = "Dhoni"
#         # print(allTrainers)

#     def Management(self):
#         self.allManagament = ("Ravi","Anji","Teja","Madhu")
#         self.favFood = "Biriyani"
#         # print(allManagament)
        
# obj = Institute()

# print("___________Details___________")

# print("BatchName:",batchName)
# print("TotalStudents:",totalstudents)

# btachstartdate()
# print("Institute Name:",obj.name)
# print("Location:",obj.loc)
# print("course:",obj.course)
# print("Fee:",obj.fee)

# obj.Trainers()
# print("Trainers:", obj.allTrainers)
# print("Crickter:",obj.cricketer)

# obj.Management()
# print("Managaent:",obj.allManagament)
# print("FavFood:",obj.favFood)

# bank_name = "SBI"
# Branch = "Kondapur"

# class Bank:

#     def __init__(self):
#         self.account_holder = "Venkatesh"
#         self.account_number = "200320062209"
#         self.account_type = "savings"
#         self.account_balance = "5000"

#     def customer_details(self):
#         self.age = 22 
#         self.city = "Hyderbad"

# obj = Bank()

# print("Bank Name:",bank_name)
# print("Branch:",Branch)

# print("Account Holder:",obj.account_holder)
# print("Account Number:",obj.account_number)
# print("Account Type:",obj.account_type)
# print("Balance:",obj.account_balance)

# obj.customer_details()

# print("Age:",obj.age)
# print("City:",obj.city)



