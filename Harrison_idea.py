from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os

# Global Variables
usersFile = "accounts.txt"
loginInfo = "pass.txt"
Harrison_usernameFile = "D:\PasswordManager_Usernames.txt"
Harrison_passwordFile = "D:\PasswordManager_Passwords.txt"

# Login Loop
close = True
while close:
    validated = False
    os.system("cls")
    print("'q' to quit or 'signin' to sign in.\n")
    option = input()
    
    # quit
    if option == 'q':
        break
    
    # Login
    if option == 'signin':
        os.system("cls")
        print("What is your Username?\n")
        username = input()
        with open(Harrison_usernameFile) as file:
            username_found = any(username in line.split() for line in file)
        if username_found:
            os.system("cls")
            print("What is your password?\n")
            password = input()
            with open(Harrison_passwordFile) as file:
                pass_found = any(password in line.split() for line in file)
        if pass_found:
            os.system("cls")
            print("Welcome " + username + ". Type 'options' if you would like to see our options menu.\n")    
            validated = True    
            showoptions = input()

        # Menu Loop
        while validated:
            # Print menu options
            if showoptions == "options":
                os.system("cls")
                print("'1' Shows your current password.\n'2' Deletes your current password.\n'3' Adds a new password.\n'4' Shows settings options.\n'5' Switches User.\n'6' Exits the program.\n")
                option = input()
            # Shows Password
            if '1' == option:
                pass
            # Delete Password
            if '2' == option:
                pass
            # Adds Password
            if '3' == option:
                pass
            # Settings
            if '4' == option:
                pass
            # Switch User
            if '5' == option:
                validated = False
            # Exit
            if '6' == option:
                close = False
                validated = False
                os.system("cls")
        if not close:
            break