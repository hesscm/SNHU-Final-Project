import os
import hashlib
import re

#Algorithm to encrypt the password
def hashAlgorithm(username, password, role):
    salt = os.urandom(32) # a new salt for this user for enhanced security

    #pbkdf2 function for slower log in, therefore deterring brute force attacks
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    #add username, salt, key, and role to credentials file. Separated by tab
    fileappend = open("credentials.txt", "a")
    fileappend.write(username + "\t" + str(salt) + "\t" + str(key) + "\t" + role + "\n")
    fileappend.close()

#Check to see if the username is already taken
def checkUserName(username):
    with open("credentials.txt") as myfile:
        lines = myfile.readlines()

    i = 0
    for userList in lines:
        userList = re.split('\t', lines[i].replace('\n', '')) #line split into a list, eliminate the new line at the end of the user
        if username == userList[0]:
            print("Username already taken")
            return True
        i += 1
    return False

#Main function for creating a new user
def createNewUser():

    while True:
        username = input("Create your username: ")
        check = checkUserName(username)
        if check == True:
            print("Please try a different username.")
        else:
            break #try again

    password = input("Create a password: ")
    confirmPassword = input("Confirm your password: ")

    #ensure user did not type an error in password
    if password == confirmPassword:
        while True:
            try:
                print("\nPlease select your role.")
                print("1. Administrator ")
                print("2. Zookeeper")
                print("3. Veterinarian")

                selection = int(input("Select your role: "))
                if selection == 1:
                    #users should not be allowed to create their own administrator account
                    print("Please contact an administrator to establish your account.")
                    role = "failure"
                    break
                elif selection == 2:
                    role = "zookeeper"
                    hashAlgorithm(username, password, role) #store encrypted information on credentials file
                    print("\n***Your account has been created.***\nWe are now transitioning you to the zookeeper menu...\n")
                    break
                elif selection == 3:
                    role = "veterinarian"
                    hashAlgorithm(username, password, role)
                    print("\n***Your account has been created.***\nWe are now transitioning you to the veterinarian menu...\n")
                    break
                else:
                    print("\nPlease enter a valid number.")
            except ValueError:
                print("\nInput failed. Please type an integer.")
    else:
        print("Passwords did not match. Please restart and try again.")
        role = "failure"

    return role #determine which menu to open next