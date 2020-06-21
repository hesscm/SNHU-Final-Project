import bottle
import json
import pprint
from bson import json_util
from pymongo import MongoClient

#Connect to local host, zoo database, and employees collections
connection = MongoClient('localhost', 27017)
db = connection['zoo'] 
employees = db['employees']

#Create a new document
def insert_document():
    print("\nNow creating the employee in the database. Please enter the appropriate data for the new employee.\n")

    id = input("Enter ID #: ")
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    role = input("Enter Role: ")
    userName = input("Enter Username: ")

    newDocument = {"ID" : id, "First Name" : firstName, "Last Name" : lastName, "Role" : role,
                    "Username" : userName}

    employees.insert_one(newDocument)    
    result = employees.find_one({"ID": id})
    pprint.pprint(result) #use pprint for better readability
    print("New employee document creation successful!")

#Search database for requested documents. 
def find_documents(choice):
    #find by name
    if choice == 1:
        employeeName = str(input("Enter an employee's exact name: "))
        result = employees.find_one({"Name": employeeName})
        pprint.pprint(result)
    #find all employees
    elif choice == 2:
        for x in employees.find().sort("ID"):
            pprint.pprint(x)
    else:
        print("An error has occured. Please try again.")

#Update a document with the user specified attributes
def update_document():
    #Choose the employee to update
    while True:
        print("\nPlease enter the ID of the employee you wish to update.\n")
        useremployee = input("employee ID: ")
        employeeToUpdate = {"ID" : useremployee}
        result = employees.find_one(employeeToUpdate)
        pprint.pprint(result)

        #Ensure correct entry
        print("\nIs this the correct entry? Type 'yes' to confirm.\n")
        confirm = input("Confirm: ")

        if confirm == "yes":
            #Choose attribute to update
            print("\nPlease enter the attribute of the employee you would like to update.")
            updatedAttribute = input("Enter title of attribute: ")

            updateView = employees.find_one(employeeToUpdate, {"_id" : 0, updatedAttribute : 1})
            print("You want to update: " + str(updateView))

            entry = input("Updated data: ")
            print("")
            print(entry)

            #Send new update to MongoDB and print confirmation to screen
            newUpdate = {"$set" : {updatedAttribute : entry}}
            print(newUpdate)
            employees.update_one(employeeToUpdate, newUpdate)
            newResult = employees.find_one(employeeToUpdate)
            pprint.pprint(newResult)
            break

        else:
            print("Please try again.")
        

#Delete a document
def delete_document():

    deleteID = input("Please enter the ID of the employee you wish to delete: ")
    print("\nYou are about to permanently delete the following employee: \n")
    result = employees.find_one({"ID": deleteID})
    pprint.pprint(result)

    #Deletions are permanent in MongoDB, check to ensure user has made the correct choice
    print("\n***Once deleted, this entry CANNOT be recovered. To confirm deletion, please type 'delete'. Enter anything else to cancel.***\n")
    confirm = input("Confirm deletion: ")
    if confirm == "delete":
        employees.delete_one({"ID" : deleteID})
        print("Your entry has been permanently deleted.")
    else:
        print("Deletion canceled. Returning to the previous menu.")