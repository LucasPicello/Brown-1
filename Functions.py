import time

def login():
    set_name = 0
    set_password = 0
    x = False
    while x == False:
        print(" ")
        print("1: have a account? login!")
        print("2: No account? create one!")
        C2 = int(input())
        if C2 == 1:
            name = input("Username: ")
            password = input("Password: ")
            if name == set_name and  password == set_password:
                x = True
            else:
                print(" ")
                print("wrong login details")
        if C2 == 2:
            set_name = input("Create a username: ")
            set_password = input("Create a password: ")
            print(" ")
            print("Account suceffully created! Now login.")
            print(" ")

def menu():
    print("____________________")
    print("    Welcome to      ")
    print("    *bookface*      ")
    print("____________________")
    print("")
    time.sleep(2)
    print(" ")

def Run():
    V = False
    Members = ["Jonh","Velma","Anderson"]
    Friends = [0,0,0]
    F = 1
    while V == False:
        print(" ")
        print("1: members online")
        print("2: friends list ")
        print("3: Exit")
        print("4: Edit login details")
        print(" ")
        C3 = int(input())
        if C3 == 4:
            print(" ")
            set_name = input("Change Username: ")
            set_password = input("Change password: ")
            print("")
            print("name changed to ", set_name)
            print("password changed to ", set_password)
        if C3 == 1:
            print("")
            print(Members)
            print(" ")
            C4 = int(input())
            if C4 == 1 and Members[0] != "Member blocked":
                print(Members[0])
                print("1: Add friend")
                print("2: block Member")
                print("3: back")
                C5 = int(input())
                if C5 == 1:
                    Friends[0] = Members[0]
                    F = F + 2
                    print("Friend sucefully added")
                if C5 == 2:
                    Members[0] = "Member blocked"
                    print("member succefully blocked")
            elif C4 == 1 :
                print("This member is blocked")
            if C4 == 2 and Members[1] != "Member blocked":
                print(Members[1])
                print("1: Add friend")
                print("2: block Member")
                print("3: back")
                C5 = int(input())
                if C5 == 1:
                    Friends[1] = Members[1]
                    F = F + 2
                    print("Friend sucefully added")
                if C5 == 2:
                    Members[1] = "Member blocked" 
                    print("member succefully blocked")
            elif C4 == 2:
                print("This member is blocked")
            if C4 == 3 and Members[2] != "Member blocked":
                print(Members[2])
                print("1: Add friend")
                print("2: block Member")
                print("3: back")
                C5 = int(input())
                if C5 == 1:
                    Friends[2] = Members[2]
                    F = F + 2
                    print("Friend sucefully added")
                if C5 == 2:
                    Members[2] = "Member blocked"
                    print("member succefully blocked")
            elif C4 == 3:
                print("this member is blocked")
        if C3 == 2:
            print(Friends)
            C4 = int(input())
            if Friends[C4-1] != 0:
                print("1: Message friend")
                print("2: Back")
                C5 = int(input())
                if C5 == 1:
                    print("To exit chat press 1")
                    R = 0
                    while R == 0:
                        Chat = input()
                        if Chat == "1":
                            R = 1
        if C3 == 3:
            print(" ")
            print("I coded all of this and you want to exit? :(")
            V = True







