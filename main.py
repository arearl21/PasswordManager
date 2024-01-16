from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256
from Crypto.Util.py3compat import b
import os
import time


# Global Variables
defaultPath = "D:/PasswordManagerFiles/"
usersFile = "accounts.txt"
passwordFile = "pass.txt"


def hashFunction(o):
    hashObject= SHA3_256.new(data=b(o))
    return hashObject.hexdigest()


def addUser(username, password):
    with open(defaultPath+usersFile) as users:
        for line in users:
            if line == username:
                os.system("cls")
                print("Username Taken. Please enter a different username.\n")
                time.sleep(2)
                return "Fail"
    with open(defaultPath+usersFile, "a") as users:
        users.write('\n'+username)
    with open(defaultPath+passwordFile, "a") as passwords:
        passwords.write('\n'+hashFunction(password))

def login():
    close = True
    while close:
        os.system("cls")
        print("Hello welcome to the AE_HT_PassManager! Are you a new user?\n\nType 'yes', 'no', or 'quit'.\n")
        option = input()
        
        # quit
        if option == 'quit':
            os.system("cls")
            break
        
        # Login
        if option == 'no':
            logged_in = False
            while logged_in == False:
                os.system("cls")
                print("What is your username?\n")
                username = input()
                if username == 'quit':
                    break
                with open(defaultPath+usersFile) as file:
                    username_found = any(username in line.split() for line in file)
                os.system("cls")
                print("What is your password?\n")
                password = input()
                with open(defaultPath+passwordFile) as file:
                    pass_found = any(password in line.split() for line in file)
                if username_found and pass_found:
                    os.system("cls")
                    print("Welcome " + username + ". Type 'options' if you would like to see our options menu.\n\nOtherwise, type 'quit'.\n")   
                    logged_in = True 
                    return True
                else:
                    os.system("cls")
                    print("Username or Password is not correct. Please try again or type 'quit'.")
                    time.sleep(3.25)
        elif option == 'yes':
            os.system("cls")
            print("Would you like to create an account with us to manage your passwords?\n\nType 'yes' or 'no'.\n")
            create_account = input()
            if create_account == 'yes':
                user_added = False
                while user_added == False:
                    os.system("cls")
                    print("Username:\n")
                    new_user = input()
                    os.system("cls")
                    print("Password:\n")
                    new_pass = input()
                    if addUser(new_user, new_pass) == "Fail":
                        pass
                    else: 
                        user_added = True
                        os.system("cls")
                        print("Welcome " + new_user + ". Type 'options' if you would like to see our options menu.\n\nOtherwise, type 'quit'.\n")   
                        return True   
            elif create_account == 'no':
                os.system("cls")
                print("You have declined the add user option. Returning to home screen...\n")
                time.sleep(3.25)  
            else:
                os.system("cls")
                print("Error. Please select one of the options. Returning to home screen...\n")
                time.sleep(2.75)
        else:
            os.system("cls")
            print("Error. Please select one of the options. Returning to home screen...\n")
            time.sleep(2.75)

def options():
    validated = True
    while validated:
        # Print menu options
        option = input()
        if option == "options":
            os.system("cls")
            print("'1' Shows your current password.\n'2' Deletes your current password.\n'3' Adds a new password.\n'4' Shows settings options.\n'5' Switches User.\n'6' Exits the program.\n")
        # Shows Password
        elif '1' == option:
            pass
        # Delete Password
        elif '2' == option:
            pass
        # Adds Password
        elif '3' == option:
            pass
        # Settings
        elif '4' == option:
            pass
        # Switch User
        elif '5' == option:
            validated = False
        # Exit
        elif '6' == option:
            validated = False
            os.system("cls")
        elif option == 'quit':
            validated = False
            os.system("cls")
        else:
            os.system("cls")
            print("Error. Returning to options menu...")
            time.sleep(2)
            os.system("cls")
            print("'1' Shows your current password.\n'2' Deletes your current password.\n'3' Adds a new password.\n'4' Shows settings options.\n'5' Switches User.\n'6' Exits the program.\n")
def main():
    if login():
        options()
    
if __name__=="__main__":
    main()