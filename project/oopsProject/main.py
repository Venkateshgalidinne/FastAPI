import json

i = int(input("choose 1.Register 2.Login  3.Logout"))


def read_json_file():
    with open ("reg_user_data.json","r") as r_file:
        user = json.load(r_file)
        print(type(user))
        return(user)

def Register():
    n = input("Enter the Name :")
    e = input("Enter the Email :")
    p = input("Enter the Password :")
    c_p = input("Enter the C_Password :")
    new_reg_user_data = {
        "Name" :n,
        "Email" : e,
        "Password" :p,
        "c_Password" : c_p
    }

    try:
        user = read_json_file()
    except FileNotFoundError :
        user = []
        print("You are trying to read un-defined file")


    if new_reg_user_data["Password"] == new_reg_user_data["c_Password"]:
        user.append(new_reg_user_data)
        print(user)
        with open ("reg_user_data.json","w") as w_file:
            json.dump(user,w_file)

        print("user added sucessfully to db")


# def login():
#     e= input("Enter the Email :")
#     p = input("Enter the Password :")

#     user = read_json_file()


#     for index,user in enumerate(user):
#         if e == user["Email"] and p ==["Password"]:
#             print(index)
#             print("Login sucessfully")
#             print("1.Edit your Profile 2.Delete your Profile")
#             i1 = input("Choose 1 Edit or 2 Delete")
#             if i1 == "1":
#                 pass
#             elif i1 == "2":
#                 user.pop(index)

#                 with open ("reg_user_data.json","w") as W_file:
#                     json.dump(user,W_file)
#             break
#         else:
#             continue
#     else:
#         print("User not Found")

# def logout():
#     print("Logout Sucessfully")

    
































# if i == 1:
#   Register()
# elif i==2:
#     login()
# else:
#     logout()    