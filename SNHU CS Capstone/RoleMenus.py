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
    print("\n***Please select an option***")
    print("1. View an Animal")
    print("2. Edit an Animal")
    print("3. Insert a New Animal")
    print("4. Delete an Animal")
    print("5. Quit")
    print(role)
   
  

    while(True):
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                search_animal(role)
                break
            elif choice == 2:
                print("FIX ME")
                break
            elif choice == 3:
                print("FIX ME")
                break
            elif choice == 4:
                print("FIX ME")
                break
            elif choice == 5:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")
          
def admin_menu(role):
    print("\n***Please select an option***")
    print("1. Search for a Specific User")
    print("2. View All Users")
    print("3. View Zookeeper Menu")
    print("4. View Veterinarian Menu")
    print("5. Quit")

    while(True):
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                print("FIX ME")
                break
            elif choice == 2:
                print("FIX ME")
                break
            elif choice == 3:
                zookeeper_menu(role)
                break
            elif choice == 4:
                veterinarian_menu(role)
                break
            if choice == 5:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")

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
                print("edit_animal()")
                break
            elif choice == 3:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")


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
                print("FIX ME")
                break
            elif choice == 2:
                print("FIX ME")
                break
            elif choice == 3:
                print("FIX ME")
                break
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
