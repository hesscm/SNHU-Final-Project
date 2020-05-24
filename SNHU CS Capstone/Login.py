import os
import hashlib
import re

#Get username and password
def getCredentials():
    userName = input("Enter user name: ")
    userPassword = input("Enter password: ")
    return userName, userPassword


#Existing user login attempt main function
def loginAttempt():
    attemptCounter = 3 #track attempts

    while(attemptCounter > 0):
        username, password = getCredentials()

        with open("credentials.txt") as myfile:
            lines = myfile.readlines()

        #iterate through lines variable, which contains all data in credentials.txt to search for matching credentials
        i = 0
        for userList in lines:
            userList = re.split('\t', lines[i].replace('\n', '')) #line split into a list, eliminate the new line at the end of the user
            new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), eval(userList[1]), 100000)

            #check if username and hash match
            if username == userList[0] and new_key == eval(userList[2]):
                print("\nLogin successful!\n")
                role = (userList[3])
                return role
            else:
                if attemptCounter == 3:
                    print("Incorrect user name and password. You have 2 attempts remaining. Please try again.")
                    attemptCounter -= 1
                    break
                elif attemptCounter == 2:
                    print("Incorrect user name and password. You have 1 attempt remaining. Please try again.")
                    attemptCounter -= 1
                    break
                else:
                    print("You have exceeded the allowed log in attempts. Exiting program...")
                    return attemptCounter
            i += 1

