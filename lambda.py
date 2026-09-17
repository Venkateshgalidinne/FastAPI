# Lambda Function:
# it is a short hand for normal def functions in python.
# a = lambda(x,y): x + y
# print(a(10,20,30))

# a = lambda *h : h
# print(a(10,20,30))

# lambda + if else:

# a = int(input("enter the Number : "))
# res = lambda xyz:"even" if xyz % 2 == 0 else "non even"

# print(res(a))

# lambda + ifelse + parameter:
# a = int(input("enter the Number : "))
# res = lambda xyz : ("even" if xyz % 2 == 0 else "non even",xyz)
# print(res(a))

# comprehension:
# list  []
# tuple
# set
# dict {}

# res = [i*2 for i in range(1,11)]
# res2 = [i**2 for i in range(1,11)]
# print(res)
# print(res2)

# lambda + list comprehension:
# res = lambda x,y:[print(i) for i in range(x,y)]
# res(1,11)

# # lambda + dict compreension:
# d = lambda incoming_dict:{print(i) for i in incoming_dict.items()}
# d({"id":1,"name":"venkatesh"})

# lambda + map:
# map() is used to apply a function to every element in a list (or any iterable).
# syntax:map(function, iterable)

# num = [1,2,3,4,5,6,7,8,9,10]
# res = list(map(lambda x : x * 3, num))
# print(res)

# marks = [75,88,92,65,77,88]
# updated_marks = list(map(lambda mark : mark + 5,marks))
# print(updated_marks)

# lambda + filter:
# filter() is used to select only the items that satisfy a condition.
# syntax: filter(function,iterables)

# marks = [23,36,45,50,65,77,88,99]

# p = list(filter(lambda m:m>=50,marks))
# print(p)



