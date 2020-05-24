
import os
import hashlib
import re
#username = input("enter a username: ") 
#password = input("enter a password: ") 


## add a user

#salt = os.urandom(32) # a new salt for this user
#key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
#fileappend = open("credentialstest.txt", "a")
#fileappend.write(username + "\t" + str(salt) + "\t" + str(key) + "\n")
#fileappend.close()




#Verification attempt 1 (incorrect password)
username = input("Enter a username: ") #jim
password = input("Enter a password: ") #pass



with open("credentialstest.txt") as myfile:
    lines = myfile.readlines()


i = 0
for userList in lines:
    userList = re.split('\t', lines[i].replace('\n', '')) #line split into a list, eliminate the new line at the end of the user
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), eval(userList[1]), 100000)
    if username == userList[0] and new_key == eval(userList[2]):
        print("found it")
        print(userList[3])
        break
    else:
        print("nope")
    i += 1

#jim pass
#jack jill
#jill cunt





