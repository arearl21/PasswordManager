from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256
from Crypto.Util.py3compat import b
import os

# Global Variables


defaultPath = "D:/PasswordManagerFiles/"
usersFile = "accounts.txt"
passwordFile = "pass.txt"


def hashFunction(o):
    hashObject= SHA3_256.new(data=b(o))
    return hashObject.hexdigest()


def addUser(username, password):
    path = defaultPath+usersFile
    print(path)
    with open(path) as users:
        for line in users:
            if line == username:
                print("Username Taken\n")
                return
        users.write(username+'\n')
    with open(defaultPath+passwordFile) as passwords:
        passwords.write(hashFunction(password)+'\n')


# Login Loop
close = True
while close:
    validated = False
    print("\'quit\' to close \nEnter Username\n Password")
    option = input()
    if option == 'quit':
        break
    if option == 'A':
        addUser(input("Enter Username:"),input("Enter Password:"))
    # Login check
    if option == '2':
        validated = True

    # Menu Loop
    while validated:
        # Print menu options
        print("options menu")
        option = input()
        # Shows Password
        if '1' == option:
            pass
        # Add Password
        if '2' == option:
            pass
        # Delete Password
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
    if not close:
        break