# Inheritance:
# Inheritance is a oops concpets where one class can acquires the properties and methods of another class.

    #             Parent
    #               ↓
    #       Common properties
    #               ↓
    #             Child
    #               ↓
    #    Reuses parent's properties

# syntax:
# class Parent:
#     # properties and methods
#     pass


# class Child(Parent):
#     # additional properties and methods
#     pass

# class Parent:

#     def house(self):
#         print("Parent owns the house")

# class child(Parent):

#     def car(self):
#         print("child owns the car ")

# obj = child()

# obj.house()
# obj.car()

# class Institute:

#     def institute_name(self):
#         print("Institute: 1000coders")

#     def Location(self):
#         print("Location: Road Number 3 KPHB ,Hyderbad")

# class Student(Institute):

#     def Student_name(self):
#         print("Student Name: Venkatesh")

# obj = Student()

# obj.institute_name()
# obj.Location()
# obj.Student_name()

# Type of Inheritances:
# 1.Single Level Inheritances
# 2.Multilevel Inheritances
# 3.Multiple level Inheritance
# 4.Hierarchial Inheritances
# 5.Hybrid Inheritances

# 1.Single Level Inheritances:
# when one child class inherits from one parent class is called single level Inheritances.

# class Animal:

#     def eat(self):
#         print("Animals eat food")

# class Dog(Animal):
    
#     def dog(self):
#         print("Dog can Barks")

# obj = Dog()
# obj.eat()
# obj.dog()


# class vehicle:

#     def start(self):
#         print("Vehicle is started")

# class Car(vehicle):

#      def drive(self):
#          print("Car is started")

# obj = Car()
# obj.start()
# obj.drive()

# class Brahmaiah:

#     surName = "Galidinne"

#     def __init__(self,inc_v1,inc_v2):
#         print(inc_v1,inc_v2)

#     def color(self):
#         c = "white"
#         print("Color:", c)

#     def Iq(self):
#         iq = 150
#         print("IQ:",iq)

# class Venkatesh(Brahmaiah):

#     def __init__(self, x,y):
#         super().__init__(x,y)
#         print(super().surName)
#         super().color()
#         super().Iq()

# obj = Venkatesh(22,9)

# class Venkateshson(Venkatesh):

#     def __init__(self, x, y):
#         super().__init__(x, y)



# v1 = Venkateshson(25, 10)
# v2 = Venkateshson(30, 11)

# class Employee:

#     def __init__(self,Name,salary):
#         self.name = Name
#         self.salary = salary

#     def display_Employee(self):

#         print("Employee Name:",self.name)
#         print("Salary:",self.salary)

# class Developer(Employee):

#     def __init__(self, Name, salary,Language):
#         super().__init__(Name, salary)
#         self.language =Language

#     def write_code(self):
#         print(self.name,"Write",self.language,"Code")

# developer = Developer(
#     "Venkatesh",
#     300000,
#     "Python"
# )

# developer1 = Developer(
#     "Sai Krishna",
#     5000000,
#     "Java"
# )

# developer.display_Employee()
# developer.write_code()
# print()
# developer1.display_Employee()
# developer1.write_code()


# class Food:

#     def __init__(self,Name,Price):
#         self.name = Name
#         self.price = Price

#     def display_food(self):
#         print("Food:",self.name)
#         print("Price:",self.price)

# class Biryani(Food):

#     def __init__(self, Name, Price,Quanity):
#         super().__init__(Name, Price)
#         self.quanity = Quanity

#     def display_bill(self):
#         total = self.price * self.quanity

#         print("Food:",self.name)
#         print("Price:",self.price)
#         print("Quanity:",self.quanity)
#         print("Total:",total)

# order = Biryani(
#     "Biryani",
#     299,
#     3
# )

# order.display_bill()


# 2.Multilevel Inheritances
# When a class inherits from another class, and a third class inherits from that child class, it is called multilevel inheritance.

# Grandparent
#      ↓
#    Parent
#      ↓
#    Child

# class Grandfather:

#     def house(self):
#         print("Grandfather Own's the house")

# class Father(Grandfather):

#     def car(self):
#         print("Father Own's the car")

# class Son(Father):

#     def Bike(self):
#         print("Son own's the Bike")

# obj = Son()

# obj.house()
# obj.car()
# obj.Bike()


# class Person:

#     def __init__(self,name,age):
#         self.Name = name
#         self.Age = age

#     def display_person(self):
#         print("Name:",self.Name)
#         print("Age:",self.Age)

# class Employee(Person):

#     def __init__(self, name, age,Salary,EmpID):
#         super().__init__(name, age)
#         self.salary = Salary
#         self.EmpID = EmpID

#     def display_employee(self):
#         print("Salary:",self.salary)
#         print("EmpID:",self.EmpID)

# class Developer(Employee):

#     def __init__(self, name, age, Salary,EmpID,Language):
#         super().__init__(name, age, Salary,EmpID)
#         self.Language = Language

#     def display_developer(self):
#         print("Programming Language:",self.Language)

# developer = Developer(
#     "Venkatesh",
#     22,
#     50000,
#     "EMPID2209",
#     "Python"
# )

# developer1 = Developer(
#     "Sai",
#     25,
#     80000,
#     "EmpID1139",
#     "Java"
# )

# developer.display_person()
# developer.display_employee()
# developer.display_developer()

# print()

# developer1.display_person()
# developer1.display_employee()
# developer1.display_developer()


# class vehicle:

#     def __init__(self,Brand,Speed):
#         self.brand = Brand
#         self.speed = Speed

#     def display_vehicle(self):
#         print("Brand:",self.brand)
#         print("Speed:",self.speed)

# class Car(vehicle):

#     def __init__(self, Brand, Speed,Model,Capacity):
#         super().__init__(Brand, Speed)
#         self.model = Model
#         self.capacity = Capacity

#     def display_car(self):
#         print("Model:",self.model)
#         print("Capacity:",self.capacity)

# class Sportcar(Car):
#     def __init__(self, Brand, Speed, Model, Capacity,Horsespower):
#         super().__init__(Brand, Speed, Model, Capacity)
#         self.horsespower = Horsespower

#     def display_sportcar(self):
#         print("Horsespowers:",self.horsespower)

# Types = Sportcar(
#     "BMW",
#     "200/min",
#     "5LWB",
#     "5 Members",
#     "255hp"
# )

# Types.display_vehicle()
# Types.display_car()
# Types.display_sportcar()

# class User:
#     def __init__(self,Name,Mobile):
#         self.name = Name
#         self.mobile = Mobile

#     def display_user(self):
#         print("Name:",self.name)
#         print("mobile:",self.mobile)

# class Customer(User):
#     def __init__(self, Name, Mobile,Address):
#         super().__init__(Name, Mobile)
#         self.Address = Address

#     def display_customer(self):
#         print("Address:",self.Address)

# class Zepto_order(Customer):
#     def __init__(self, Name, Mobile, Address,Product,Quantity,Price):
#         super().__init__(Name, Mobile, Address)
#         self.product = Product
#         self.quantity = Quantity
#         self.price = Price
#     def display_order(self):
    
#         print("Product:",self.product)
#         print("Quantity:",self.quantity)
#         print("Price:",self.price)
        

#     def display_bill(self):
#          Total = self.quantity * self.price
#          print("Total Bill:",Total)


# Delivery = Zepto_order(
#     "Venkatesh",
#     9705695719,
#     "1-57-299 Kondapur",
#     "Milk",
#     2,
#     90

# )

# Delivery1 = Zepto_order(
#     "Krishna",
#     9542177035,
#     "1-77-199 Manikonda",
#     "Tomatos",
#     3,
#     49.3
# )

# print("--------Order-1-------")
# Delivery.display_user()
# Delivery.display_customer()
# Delivery.display_order()
# Delivery.display_bill()

# print("------Order-2--------")
# Delivery1.display_user()
# Delivery1.display_customer()
# Delivery1.display_order()
# Delivery1.display_bill()

# MultipleLevel Inheritances:
# Multiple level Inheritances mean one child class inherits from one or more parent classes.

# Parent 1       Parent 2
#     \             /
#      \           /
#        Child

# class Father:

#     def house(self):
#         print("Father own's the House")

# class Mother:

#     def Car(self):
#         print("Mother own's the Car")

# class child(Father,Mother):

#     def Bike(self):
#         print("Child OWn's the bike")

# s = child()

# s.house()
# s.Car()
# s.Bike()
              
# class Camera:

#     def photo(self):
#         print("Take a Photo")

# class Phone:

#     def call(self):
#         print("Making a Phone call")

# class SmartMobile(Camera,Phone):

#     def Internet(self):
#         print("use Internet for Anything")

# M = SmartMobile()
# M.photo()
# M.call()
# M.Internet()

# class Employee:

#     def __init__(self,Name,Salary):
#         self.name =Name
#         self.Salary = Salary

#     def display_employee(self):
#         print("Employee Name:",self.name)
#         print("Salary:",self.Salary)

# class managing_Skills:

#     def managing_skills(self):
#         print("Managaing the Team")

# class Manager(Employee,managing_Skills):

#     def display_manager(self):
#         print("Manager:", self.name)

# E = Manager("Venkatesh",50000)

# E.display_employee()
# E.managing_skills()
# E.display_manager()
    
# class Product:

#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#     def display_product(self):
#         print("Name:",self.name)
#         print("Price:",self.price)

# class Inventory:
#      def Check_stock(self):
#          print("Product is available")

# class Order:

#     def place_order(self):
#         print("Order is placed successfully")

# class ShoppingProduct(Product,Inventory,Order):
#     pass

# items = ShoppingProduct("Laptop",75999)

# items.display_product()
# items.Check_stock()
# items.place_order()

# class PersonalDetails:

#     def __init__(self,Name,Age):
#         self.name = Name
#         self.age = Age
        
#     def display_Personl(self):
#         print("Name:",self.name)
#         print("Age:",self.age)

# class AcademicDetails:

#     def __init__(self,course,marks,grade):
#         self.Course = course
#         self.Marks = marks
#         self.Grade = grade

#     def display_Academic(self):
#         print("Course:",self.Course)
#         print("Marks:",self.Marks)
#         print("Grade:",self.Grade)

# class student(PersonalDetails,AcademicDetails):

#     def __init__(self, Name, Age,Course,marks,grade):
#         PersonalDetails.__init__(self,Name,Age)
#         AcademicDetails.__init__(self,Course,marks,grade)

    
#     def display_studentDetails(self):
#         print("Student Information")

# s  = student("Venkatesh",22,"Python",99,"A+")

# s.display_studentDetails()
# s.display_Personl()
# s.display_Academic()

# class PersonalDetails:

#     def __init__(self,name,age,location):
#         self.Name = name
#         self.Age = age
#         self.Location = location

#     def display_personal(self):
#         print("Name:",self.Name)
#         print("Age:",self.Age)
#         print("Location:",self.Location)

# class TechnicalSkills:

#     def __init__(self,language,framework,experience):
#         self.Language = language
#         self.Framework = framework
#         self.Experience = experience

#     def display_Technical(self):
#         print("Language:",self.Language)
#         print("Framework:",self.Framework)
#         print("Experience:",self.Experience)

# class Developer(PersonalDetails,TechnicalSkills):

#     def __init__(self, name, age, location,language,framework,experience):
#         PersonalDetails.__init__(self,name,age,location)
#         TechnicalSkills.__init__(self,language,framework,experience)

#     def display_developer(self):
#         print("Developer Information")

# d = Developer(
#     "Venkatesh",
#     22,
#     "Kondapur ,Hyderbad",
#     "Python",
#     "Django",
#     7
# )
# d.display_developer()
# print("-------------------")
# d.display_personal()
# d.display_Technical()

# 4.Hierarichial Inheritances:
# hierarical Inheritances occures multiple child classes inherits from the same parent class.

        #       Parent
        #      /      \
        #     ↓        ↓
        #  Child 1   Child 2

# class Employee:

#     def __init__(self,name,salary):
#         self.Name = name
#         self.Salary = salary

#     def display_employee(self):
#         print("Name:",self.Name)
#         print("Salary:",self.Salary)

# class Developer(Employee):

#     def write_code(self):
#         print(self.Name, "Write python codes")

# class Tester(Employee):

#     def test_application(self):
#         print(self.Name,"Test the application")

# developer = Developer("Venkatesh",50000)
# tester = Tester("Revanth",60000)

# print("-----Developer-------")
# developer.display_employee()
# developer.write_code()

# print("------Tester------")
# tester.display_employee()
# tester.test_application()        

# class BankAccount:

#     def __init__(self,Name,Balance):
#         self.name = Name
#         self.balance = Balance

#     def display_account(self):
#         print("Account Holder:",self.name)
#         print("Balance:",self.balance)

# class SavingsAccount(BankAccount):

#     def show_Interest(self):
#         print("Saving Account Interest: 7%")

# class CurrentAccount(BankAccount):

#     def show_overdraft(self):
#         print("Current Account Balance :$500000")

# S1 = SavingsAccount("Venkatesh",9000000)
# C1 = CurrentAccount("Sai",780000)

# print("-------Saving Account---------")

# S1.display_account()
# S1.show_Interest()

# print("--------current Account--------")

# C1.display_account()
# C1.show_overdraft()
         


    
        
