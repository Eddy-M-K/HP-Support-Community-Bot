def Get_Sign_In():
    t = open("signin.txt", "r")
    username = t.readline()
    password = t.readline()

    return username, password