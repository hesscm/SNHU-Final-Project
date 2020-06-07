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
        #iterate through credentials file to search for matching credentials
        #Stops searching when a match is found
        with open("credentials.txt") as file:
            for line in file:

                userList = re.split('\t', line.replace('\n', '')) #line split into a list, eliminate the new line at the end of the user
                new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), eval(userList[1]), 100000)

                #check if username and hash match
                if username == userList[0] and new_key == eval(userList[2]):
                    print("\nLogin successful!\n")
                    role = (userList[3])
                    return role
          
            if attemptCounter == 3:
                print("Incorrect user name and password. You have 2 attempts remaining. Please try again.")
                attemptCounter -= 1
            elif attemptCounter == 2:
                print("Incorrect user name and password. You have 1 attempt remaining. Please try again.")
                attemptCounter -= 1
            else:
                print("You have exceeded the allowed log in attempts. Exiting program...")
                return attemptCounter

