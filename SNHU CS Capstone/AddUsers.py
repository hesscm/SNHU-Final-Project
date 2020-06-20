import os
import hashlib
import re

#Algorithm to encrypt the password
def hashAlgorithm(username, password, role):
    salt = os.urandom(32) # a new salt for this user for enhanced security

    #pbkdf2 function for slower log in, therefore deterring brute force attacks
    #encodes password into a hash
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    #add username, salt, key, and role to credentials file. Separated by tab
    fileappend = open("credentials.txt", "a")
    fileappend.write(username + "\t" + str(salt) + "\t" + str(key) + "\t" + role + "\n")
    fileappend.close()

#Check to see if the username is already taken
def checkUserName(username):
    with open("credentials.txt") as myfile:
        for line in myfile:
            userList = re.split('\t', line.replace('\n', '')) #line split into a list, eliminate the new line at the end of the user
            if username == userList[0]:
                print("\nUsername already taken. Please try a different username.\n")
                return True
        return False

#Main function for creating a new user
def createNewUser(role):

    while True:
        username = input("Create your username: ")
        check = checkUserName(username)
        if check == False:
            break #move on to password creation

    password = input("Create a password: ")
    confirmPassword = input("Confirm your password: ")

    #ensure user did not type an error in password
    if password == confirmPassword:
        print("\nPlease select your role.\n")
        while True:
            try:
                print("1. Administrator ")
                print("2. Zookeeper")
                print("3. Veterinarian")

                selection = int(input("\nSelect your role: "))
                if selection == 1:
                    #users should not be allowed to create their own administrator account
                    if role != "admin":
                        print("Please contact an administrator to establish your account.")
                        role = "failure"
                        break
                    else:
                        hashAlgorithm(username, password, role) #store encrypted information on credentials file
                        print("\n***The user account has been created.***\n")
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
                print("\nInput failed. Please type an integer.\n")
    else:
        print("Passwords did not match. Please restart and try again.")
        role = "failure"

    return role #determine which menu to open next