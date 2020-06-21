#This program started as an authentication system for a zoo, written in Java, and
#has been developed in Python with more added features. Currently, this program allows
#new users to create a user ID, password, and zoo role. Once logged in, they will be redirected
#to their appropriate role's menu. The passsword is encrypted with the SHA-256 algorithm using Python's
#pbkdf2_hmac() hashing method. Users can access the MongoDB "animals" database, while the administrator
#is able to access the "employees" database.


import Login, RoleMenus, AddUsers, CRUDoperations

def main():

    print("***Welcome to the zoo computer system! Please enter your credentials to continue.*** \n***You have 3 attempts before the system logs you out.***\n")
    while True:
        
        print("Are you a new or existing user?") #Option to log in or create new account
        print("1. New User")
        print("2. Existing User")
        print("3. Quit")
        try:
            userChoice = int(input("Select an option: "))
            if userChoice == 1:
                role = "none"
                newUser = AddUsers.createNewUser(role) #Go to AddUsers module
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
            else:
                print("\nPlease enter a valid number.")
        except ValueError:
            print("Input failed. Please type an integer.")

        print()

#Start program, print text upon exit of program      
main()
print("Goodbye!")
        