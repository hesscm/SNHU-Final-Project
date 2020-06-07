#This program started as an authentication system for a zoo, written in Java, and
#has been developed in Python with more added features. Currently, this program allows
#new users to create a user ID, password, and zoo role. Once logged in, they will be redirected
#to their appropriate role's menu. The passsword is encrypted with the SHA-256 algorithm using Python's
#pbkdf2_hmac() hashing method. 
#Still to be added: Polishing, more exception checks, reduce redundancies, create employees collection

import Login, RoleMenus, AddUsers, CRUDoperations
import os

#I had trouble getting Visual Studio to recognize the correct directory so I used this command to change the directory
#os.chdir(r"C:\Users\Hess\source\repos\hesscm.github.io\SNHU CS Capstone")

def main():

    while True:
        print("Welcome to the zoo computer system! Please enter your credentials to continue. You have 3 attempts before the system logs you out.\n")
        print("Are you a new or existing user?") #Option to log in or create new account
        print("1. New User")
        print("2. Existing User")
        print("3. Quit")
        try:
            userChoice = int(input("Select an option: "))
            if userChoice == 1:
                newUser = AddUsers.createNewUser() #Go to AddUsers module
                if newUser == "failure": #Exit loop and exit program
                    break
                RoleMenus.readFile(newUser) #Account creation successful, log in to role
                break
            elif userChoice == 2:
                loginAttempts = Login.loginAttempt() #Existing users log in with Login module
                if loginAttempts == 1: #Login attempts exceeded, exit program
                    break
                RoleMenus.readFile(loginAttempts) #Log in to role and view its menu/submenus
                break
            elif userChoice == 3:
                break
            elif userChoice == 4:
                CRUDoperations.test()
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Input failed. Please type an integer.")

        print()

#Start program, print text upon exit of program      
main()
print("Goodbye!")
        