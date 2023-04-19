import re
password = str(input("enter password: "))
flag = 0

while True:
    if len(password) < 8:
        flag = -1
        print("Passing length is less than 8")
        break
    elif len(password) > 16:
        flag = -1
        print("Passing length is more than 16")
        break
    elif not re.search(r"[a-z]", password): 
        flag = -1
        print("Passing must contain a lowercase letter")
        break
    elif not re.search(r"[A-Z]", password): 
        flag = -1
        print("Passing must contain an Uppercase letter")
        break
    elif not re.search(r"[0-9]", password): 
        flag = -1
        print("Passing must contain a number")
        break
    elif not re.search(r"[ !#$%&'()*+,-\./[\\\]^_`{|}~]", password): 
        flag = -1
        print("Password must contain a special character")
        break
    for i in range(len(password)-1): 
        if password[i] == password[i+1]:
            flag = -1
            print("Password must not have two consecutive characters that are same")
            break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")
