#Obtain role from main, open welcome file depending on role and go to specific role submenu
def readFile(role):
    file = open(role + ".txt")
    print(file.read())
    file.close()
    if "zookeeper" in role:
        zookeeper_menu()
    elif "admin" in role:
        admin_menu()
    elif "veterinarian" in role:
        veterinarian_menu()
    else:
        print("FIX ROLE IN MainMenu") #need to add exception check here

#Specified CRUD options for zookeeper
def zookeeper_menu():
    print("\n***Please select an option***")
    print("1. View an Animal")
    print("2. Edit an Animal")
    print("3. Insert a New Animal")
    print("4. Delete an Animal")
    print("5. Quit")

    while(True):
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                print("FIX ME")
                break
            if choice == 2:
                print("FIX ME")
                break
            if choice == 3:
                print("FIX ME")
                break
            if choice == 4:
                print("FIX ME")
                break
            if choice == 5:
                break
            else:
                print("You did not enter a valid number. Please try again.")
        except ValueError:
            print("Input failed. Please type an integer.")
          
def admin_menu():
    return "IN DEVELOPMENT"

def veterinarian_menu():
    return "IN DEVELOPMENT"