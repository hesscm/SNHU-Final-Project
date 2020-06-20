import CRUDoperations
import AdminCRUD
import AddUsers

#Obtain role from main, open welcome file depending on role and go to specific role submenu
def readFile(role):
    file = open(role + ".txt")
    print(file.read())
    file.close()
    if "zookeeper" in role:
        zookeeper_menu(role)
    elif "admin" in role:
        admin_menu(role)
    elif "veterinarian" in role:
        veterinarian_menu(role)
    else:
        print("FIX ROLE IN MainMenu") #need to add exception check here

#Specified CRUD options for zookeeper
def zookeeper_menu(role):

    while(True):
        print("\n***Please select an option***")
        print("1. View an Animal")
        print("2. Edit an Animal")
        print("3. Insert a New Animal")
        print("4. Delete an Animal")
        print("5. Quit\n")
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                search_animal(role)
            elif choice == 2:
                CRUDoperations.update_document(role)
            elif choice == 3:
                CRUDoperations.insert_document(role)
            elif choice == 4:
                CRUDoperations.delete_document(role)
            elif choice == 5:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")
          
#Menu for administrator. Employee access information to still to be created
def admin_menu(role):

    while(True):
        print("\n***Please select an option***")
        print("1. Search for a Specific User")
        print("2. View All Users")
        print("3. Add a User")
        print("4. Update a User")
        print("5. Delete a User")
        print("6. View Zookeeper Menu")
        print("7. View Veterinarian Menu")
        print("8. Quit")
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                AdminCRUD.find_documents(choice)
            elif choice == 2:
                AdminCRUD.find_documents(choice)
            #Create user credentials and then add employee to database
            elif choice == 3:
                print("Transitioning to New User process...")
                AddUsers.createNewUser(role)
                AdminCRUD.insert_document()
            elif choice == 4:
                AdminCRUD.update_document()
            elif choice == 5:
                AdminCRUD.delete_document()
            elif choice == 6:
                zookeeper_menu(role)
            elif choice == 7:
                veterinarian_menu(role)
            elif choice == 8:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")

#Menu for veterinarian. They are only able to edit medical records.
def veterinarian_menu(role):


    while(True):
        print("\n***Please select an option***")
        print("1. View an Animal's Medical Records")
        print("2. Edit an Animal's Medical Records")
        print("3. Quit")
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                search_animal(role)
            elif choice == 2:
                CRUDoperations.update_document(role)
            elif choice == 3:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")

#Submenu to choose how the user wants to search for a document
def search_animal(role):

    print("\n***Please select an option***")
    print("1. Search for an Animal by Name")
    print("2. Search for an Animal by ID")
    print("3. View All Animals")
    print("4. Main Menu")
    print("5. Quit")

    while(True):
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                CRUDoperations.find_documents(1, role)
                break
            elif choice == 2:
                CRUDoperations.find_documents(2, role)
                break
            elif choice == 3:
                CRUDoperations.find_documents(3, role)
                break
            #Return to the user's main menu
            elif choice == 4:
                if role =="zookeeper":
                    zookeeper_menu(role)
                    break
                elif role == "veterinarian":
                    veterinarian_menu(role)
                    break
                elif role == "admin":
                    admin_menu(role)
                    break
            elif choice == 5:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")
