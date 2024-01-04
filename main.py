from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# Global Variables
usersFile = "accounts.txt"
loginInfo = "pass.txt"

# Login Loop
close = True
while close:
    validated = False
    print("\'quit\' to close \nEnter Username\n Password")
    option = input()
    if option == 'quit':
        break

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