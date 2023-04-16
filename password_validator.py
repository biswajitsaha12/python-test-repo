import re
password = str(input("enter password: "))
flag = 0

while True:
    if (len(password) < 8 or len(password) > 16): #length
        flag = -1
        break
    elif not re.search(r"[a-z]", password): #lowercase
        flag = -1
        break
    elif not re.search(r"[A-Z]", password): #uppercase
        flag = -1
        break
    elif not re.search(r"[0-9]", password): #number
        flag = -1
        break
    elif not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~]", password): #special character
        flag = -1
        break
    for i in range(len(password)-1): #consecutive characters
        if password[i] == password[i+1]:
            flag = -1
            break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")
