# for i in range(1,6):
#     print("*" * i)
# o/p:
# *
# **
# ***
# ****
# *****

# decreasing:
# for i in range(5,0,-1):   
#     print("*" * i)

# o/p:
# *****
# ****
# ***
# **
# *

# sequance:
# for i in range(8):
#     print("*" * 8)
# o\p:
# ********
# ********
# ********
# ********
# ********
# ********
# ********

# right Trainagle:
# for i in range(1,6):
#     print(" " * (5-i) + "*" * i)
# o\p:
#     *
#    **
#   ***
#  ****
# *****
# pyrmid:
# for i in range(1,6):
#     space = 5-i
#     star = 2 * i - 1
#     print(" " * space + "*" * star)

# o\p:
#     *
#    ***
#   *****
#  *******
# *********

# n=5

# for i in range(n,0,-1):
#     space = n -i
#     star = 2 * i - 1

#     print(" " * space + "*" * star)

# o\p:
# *********
#  *******
#   *****
#    ***
#     *

# n = 5
# for i in range(n):
#     if i == 0 or i == n-1 :
#         print("*" * n)
#     else:
#         print("*" + " " * 3 + "*")


# n = 8
# for i in range(n):
#     if i == 0 or i == n-1 :
#         print("*" * n)
#     else:
#         print("*" + " " * 6 + "*")

# o\p:
# ********
# *      *
# *      *
# *      *
# *      *
# *      *
# *      *
# ********

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 1
# 12
# 123
# 1234
# 12345

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# # o\p:
# 12345
# 1234
# 123
# 12
# 1

# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()

# o\p:
# 1
# 22
# 333
# 4444
# 55555

# for i in range(5, 0, -1):
#     for j in range(5 , 5-i , -1):
#         print(j, end="")
#     print()
# o\p:
# 54321
# 5432
# 543
# 54
# 5

# num = 1
# for i in range(1,6):
#     for j in range(i):
#         print(num,end="")
#         num = num+1
#     print()
# o\p:
# 1
# 23
# 456
# 78910
# 1112131415

# n = 5
# for i in range(1,n+1): #row
#     print(" " * (n-i),end="")

#     for j in range(1,2*i): #numbers
#         print(j,end="")
#     print()

# o\p:
#     1
#    123
#   12345
#  1234567
# 123456789

# n = 5
# for i in range(n,0,-1):
#     print(" " *(n-i),end="")

#     for j in range(1,2*i):
#         print(j,end="")
#     print()
# o\p:
# 123456789
#  1234567
#   12345
#    123
#     1


n = 5

# for i in range(1,n+1):
#     print(" " * (n-i),end="")

#     for j in range(1,2*i):
#         print(j,end="")
#     print()

# n = 9 
# for i in range(n,0,-1):
#     print(" " *(n-i),end="")

#     for j in range(1,2*i):
#         print(j,end="")

#     print()

# num = 1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end="")
#         num = num+1
#     print()

# n = 5

# for i in range(1, n + 1):
#     spaces = n - i
#     stars = 2 * i - 1
#     print(" " * spaces + "*" * stars)

# for i in range(n - 1, 0, -1):
#     spaces = n - i
#     stars = 2 * i - 1
#     print(" " * spaces + "*" * stars)
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

