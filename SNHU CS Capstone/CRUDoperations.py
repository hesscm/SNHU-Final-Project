import bottle
import json
import pprint
from bson import json_util
from pymongo import MongoClient

#Connect to local host, zoo database, animals and employees collections
connection = MongoClient('localhost', 27017)
db = connection['zoo'] 
animals = db['animals']
employees = db['employees']

#Create a new document
def insert_document(role):
    #Only zookeepers and admins can create documents
    if role == "zookeeper" or "admin":
        print("Please enter the appropriate data for the new animal.")
        id = input("Enter ID #: ")
        name = input("Enter Name: ")
        species = input("Enter Species: ")
        birthdate = input("Enter Birth Date: ")
        location = input("Enter Habitat Location: ")
        welfare = input("Enter General Welfare: ")
        diet = input("Enter Diet: ")
        conditions = input("Enter Habitat Conditions: ")
        height = input("Enter Height: ")
        weight = input("Enter Weight: ")
        vaccinations = input("Enter Vaccinations: ")

        newDocument = {"ID" : id, "Name" : name, "Species" : species, "Birth Date" : birthdate,
                       "Habitat Location" : location, "General Welfare" : welfare, "Diet" : diet,
                       "Habitat Conditions" : conditions, "Height" : height, "Weight" : weight, 
                       "Vaccinations" : vaccinations}

        animals.insert_one(newDocument)    
        result = animals.find_one({"ID": id})
        pprint.pprint(result) #use pprint for better readability
        print("New animal document creation successful!")
    else:
        print("You are not authorized to create a new entry.")

#Search database for requested documents. 
def find_documents(choice, role):
    #find by name
    if choice == 1:
        animalName = str(input("Enter an animal's exact name: "))
        if role == "zookeeper":                              #Specific information is only available to specific roles
            result = animals.find_one({"Name": animalName}, {"_id" : 0, "Vaccinations" : 0, "Height" : 0, "Weight" : 0})
            pprint.pprint(result)
        elif role == "veterinarian":
            result = animals.find_one({"Name": animalName}, {"_id" : 0, "Habitat Location" : 0, "Habitat Conditions" : 0})
            pprint.pprint(result)
        elif role == "admin":
            result = animals.find_one({"Name": animalName})
            pprint.pprint(result)
    #find by ID
    elif choice == 2:
        animalID = input("Enter an animal's ID: ")
        if role == "zookeeper": 
            result = animals.find_one({"ID": animalID}, {"_id" : 0, "Vaccinations" : 0, "Height" : 0, "Weight" : 0})
            pprint.pprint(result)
        elif role == "veterinarian":
            result = animals.find_one({"ID": animalID}, {"_id" : 0, "Habitat Location" : 0, "Habitat Conditions" : 0})
            pprint.pprint(result)
        elif role == "admin":
            result = animals.find_one({"ID": animalID})
            pprint.pprint(result)
    #find all animals
    elif choice == 3:
        if role == "zookeeper": 
            for x in animals.find({}, {"_id" : 0, "Vaccinations" : 0, "Height" : 0, "Weight" : 0}).sort("ID"):
                pprint.pprint(x)
        elif role == "veterinarian":
            for x in animals.find({}, {"_id" : 0, "Habitat Location" : 0, "Habitat Conditions" : 0}).sort("ID"):
                pprint.pprint(x)
        elif role == "admin":
            for x in animals.find().sort("ID"):
                pprint.pprint(x)
    else:
        print("An error has occured. Please try again.")

#Update a document with the user specified attributes
def update_document(role):
    #Choose the animal to update
    while True:
        print("\nPlease enter the ID of the animal you wish to update.\n")
        userAnimal = input("Animal ID: ")
        animalToUpdate = {"ID" : userAnimal}
        result = animals.find_one(animalToUpdate)
        pprint.pprint(result)

        #Ensure correct entry
        print("\nIs this the correct entry? Type 'yes' to confirm.\n")
        confirm = input("Confirm: ")

        if confirm == "yes":
            #Choose attribute to update
            print("\nPlease enter the attribute of the animal you would like to update.")
            updatedAttribute = input("Enter title of attribute: ")

            #security check that roles only edit authorized attributes
            if role == "veterinarian":
                if updatedAttribute not in ("Diet","General Welfare","Height","Weight","Vaccinations"):
                    print("\nYou do not have the appropriate privileges to change these attributes.")
                    continue #try again
            if role == "zookeeper":
                if updatedAttribute in ("Vaccinations"):
                    print("\nYou do not have the appropriate privileges to change these attributes.")
                    continue #try again

            updateView = animals.find_one(animalToUpdate, {"_id" : 0, updatedAttribute : 1})
            print("You want to update: " + str(updateView))

            entry = input("Updated data: ")
            print("")
            print(entry)

            #Send new update to MongoDB and print confirmation to screen
            newUpdate = {"$set" : {updatedAttribute : entry}}
            print(newUpdate)
            animals.update_one(animalToUpdate, newUpdate)
            newResult = animals.find_one(animalToUpdate)
            pprint.pprint(newResult)
            break

        else:
            print("Please try again.")
        

#Delete a document
def delete_document(role):
    #Only zookeepers and administrators can delete documents
    if role == "zookeeper" or "admin":
        deleteID = input("Please enter the ID of the animal you wish to delete: ")
        print("\nYou are about to permanently delete the following animal: \n")
        result = animals.find_one({"ID": deleteID})
        pprint.pprint(result)

        #Deletions are permanent in MongoDB, check to ensure user has made the correct choice
        print("\n***Once deleted, this entry CANNOT be recovered. To confirm deletion, please type 'delete'. Enter anything else to cancel.***\n")
        confirm = input("Confirm deletion: ")
        if confirm == "delete":
            animals.delete_one({"ID" : deleteID})
            print("Your entry has been permanently deleted.")
        else:
            print("Deletion canceled. Returning to the previous menu.")
    else:
        print("You are not authorized to create a new entry.")


