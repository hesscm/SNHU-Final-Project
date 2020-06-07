import CRUDoperations

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
        print("3. View Zookeeper Menu")
        print("4. View Veterinarian Menu")
        print("5. Quit")
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                print("FIX ME")
            elif choice == 2:
                print("FIX ME")
            elif choice == 3:
                zookeeper_menu(role)
            elif choice == 4:
                veterinarian_menu(role)
            elif choice == 5:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")

#Menu for veterinarian. They are only able to edit medical records.
#FIX ME: ENABLE SECURITY MEASURES SO VETS CANNOT EDIT OTHER ATTRIBUTES
def veterinarian_menu(role):
    print("\n***Please select an option***")
    print("1. View an Animal's Medical Records")
    print("2. Edit an Animal's Medical Records")
    print("3. Quit")

    while(True):
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                search_animal(role)
                break
            elif choice == 2:
                CRUDoperations.update_document(role)
                break
            elif choice == 3:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")

#Submenu to choose how the user wants to search for a document
#FIX ME: This method could potentially move to CRUDoperations.py
def search_animal(role):

    print("\n***Please select an option***")
    print("1. Search for an Animal by Name")
    print("2. Search for an Animal by ID")
    print("3. View All Animals")
    print("4. Previous Menu")
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
