import pandas as pd
import os


# Name: Jacob Frazer
# Student Number: 31004433
# Computer Networks


def encrypt_data():  # Section B req 2, 3 & 4

    def encrypt(key, message):
        alpha = "abcdefghijklmnopqrstuvwxyz"  # alphabet used to encrypt
        message = message
        alpha = alpha + alpha.upper()
        result = ""  # creating empty variable to store for loop as it iterates

        for letter in message:
            if letter in alpha:  # if the for loop detects a matching letter in alphabet
                letter_index = (alpha.find(letter) + key) % len(
                    alpha)  # finds index position and adds key, modulo prevents looping around the alpha string
                result = result + alpha[letter_index]
            else:
                result = result + letter
        encrypted_message = result.replace(" ", "@")  # replacing whitespace with @ symbol
        return encrypted_message

    def decrypt(key, message):
        alpha = "abcdefghijklmnopqrstuvwxyz"  # alphabet used to encrypt
        message = message
        alpha = alpha + alpha.upper()
        result = ""  # creating empty variable to store for loop as it iterates

        for letter in message:
            if letter in alpha:  # if the for loop detects a matching letter in alphabet
                letter_index = (alpha.find(letter) - key) % len(
                    alpha)  # finds index position and adds key, modulo prevents looping around the alpha string
                result = result + alpha[letter_index]
            else:
                result = result + letter
        decrypted_message = result.replace("@", " ")  # replacing @ with whitespace reversing the prior encryption
        return decrypted_message

    encrypt_data_loop = True
    while encrypt_data_loop:
        print("\n\t\t:: Encrypt/Decrypt Data ::")  # Menu
        print("-" * 42)
        print("1. Encrypt a message and save into a file")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Return to Main Menu\n")

        encrypt_data_selection = input("Select a menu - Input a number: ")
        while not encrypt_data_selection.isdigit():  # checking that main menu selection is a digit
            encrypt_data_selection = input("\nYou have entered a non digit value, Select again: ")

        if encrypt_data_selection == "1":  # req 2
            message_to_encrypt = input("\nInput a message to encrypt: ")  # allows user to input a message
            print("\nYour message is ", message_to_encrypt)  # user prompted with their message
            while True:
                try:
                    encryption_key = int(input(
                        "\nInput a number for the encryption key between 1 and 26: "))
                    while encryption_key < 1 or encryption_key > 26:
                        encryption_key = int(input(
                            "\nYou're key is out of bounds, please re enter a key between 1 and 26: "))

                    print("\nYour encryption key is: ", encryption_key)
                    print("\nEncoded Message: " + encrypt(encryption_key, message_to_encrypt))
                    print("\nMessage saved to encoded_msg.txt")
                    with open("encoded_msg.txt",
                              "w") as f:  # file handing with open allows me to not need a close statement
                        f.write(encrypt(encryption_key, message_to_encrypt))
                    break
                except ValueError:  # catching outside of boundary input
                    print("\nYou must enter a NUMBER between 1 and 26")

        elif encrypt_data_selection == "2":  # req 3
            while True:
                file_input = input("\nPlease input the file name to encrypt (format filename.txt): ")
                print()
                try:  # attempts to open file based on user input
                    with open(file_input) as file_data:
                        lines = file_data.read().strip()
                        print(lines)  # printing the file that the user has chosen
                    break
                except FileNotFoundError:  # catching file not found
                    print("File doesn't exist, Check available files or ensure correct input format filename.txt")

            while True:  # while loop with try/except block to ensure correct key and file input
                try:
                    file_encryption_key = int(input("\nInput a number for the encryption key between 1 and 26: "))
                    while file_encryption_key < 1 or file_encryption_key > 26:
                        file_encryption_key = int(input(
                            "\nYou're key is out of bounds, please re enter a key between 1 and 26: "))
                    with open("encryptedFile.txt",
                              "w") as new_encrypted_file:
                        new_encrypted_file.write(encrypt(file_encryption_key, lines))  # calling encryption function
                    print("\nEncryption applied, file saved as encryptedFile.txt ")
                    print()
                    with open("encryptedFile.txt", "r") as show_file:
                        lines = show_file.read()
                        print(lines)  # printing the newly encrypted file
                    break
                except ValueError:  # catching out of bounds input
                    print("\nYou must enter a NUMBER between 1 and 26")

        elif encrypt_data_selection == "3":  # req 4
            while True:  # while loop with try/except block to ensure correct file input
                file_input = input("\nPlease input the file name to decrypt (format filename.txt): ")
                print()
                try:
                    with open(file_input) as file_data:
                        lines = file_data.read().strip()
                        print(lines)  # printing file selected by user
                    break
                except FileNotFoundError:  # catching file not found
                    print("File doesn't exist, Check available files or ensure correct input format filename.txt")

            while True:  # while loop with try/except block to ensure correct key and file input
                try:
                    file_decryption_key = int(input("\nInput a number for the decryption key between 1 and 26: "))
                    while file_decryption_key < 1 or file_decryption_key > 26:  # entry exception handling
                        file_decryption_key = int(input(
                            "\nYou're key is out of bounds, please re enter a key between 1 and 26: "))
                    with open("decryptedFile.txt",
                              "w") as new_encrypted_file:
                        new_encrypted_file.write(decrypt(file_decryption_key, lines))  # calling decryption function
                    print("\nDecryption applied, file saved as decryptedFile.txt \n")
                    with open("decryptedFile.txt", "r") as show_file:
                        lines = show_file.read()
                        print(lines)  # prints newly decrypted file
                    break
                except ValueError:  # catches out of bounds input
                    print("\nYou must enter a NUMBER between 1 and 26")  # entry exception handling

        elif encrypt_data_selection == "4":
            print("\n\t\t  Exiting to Main Menu")
            encrypt_data_loop = False

        else:
            print("\nThere is no menu", encrypt_data_selection, "please try again")  # entry exception handling


def extract_data():  # Section C req 5, 6, 7, & 8
    extract_data_loop = True
    while extract_data_loop:
        print("\n\t\t  :: Extract Data ::")  # Menu
        print("-" * 42)
        print("1. View all Records")
        print("2. View Records by Date")
        print("3. View Records by User")
        print("4. Count User Logs")
        print("5. Return to Main Menu\n")

        extract_data_selection = input("Select a menu - Input a number: ")
        while not extract_data_selection.isdigit():  # digit exception handling
            extract_data_selection = input("\nYou have entered a non digit value, Select again: ")

        if extract_data_selection == "1":
            cols = ["\bName", "Date"]  # defining the columns using LIST
            data = pd.read_csv("data.txt", sep=",", names=cols)  # adds column header
            data.index += 1  # increments index position so index doesnt start at 0
            data.index.names = ["No"]  # index position header
            print(f"\n\t\t:: View ALl Records ::")
            print("-" * 42)
            print(data)
            print("-" * 42)

        elif extract_data_selection == "2":
            print("\n\t  :: View Records by Date ::")
            print("-" * 42)
            cols = ["Name", "Date"]  # use of list to satisfy requirement
            data = pd.read_csv("data.txt", header=None, names=cols)
            data.index.names = ["No"]  # index position header
            data.index += 1  # increments index position so index doesnt start at 0
            search = input("\nInput date using format DD/MM/YYYY: ")  # user input for date search
            date_search = data[(data["Date"] == search)]  # creating var that matches date from data and user search

            while len(date_search) == 0:  # if nothing matches while loop keeps looping
                print("\nNo Record Found! Make sure you are using the correct Date Format: DD/MM/YYYY E.G 09/09/2021")
                search = input("\ninput date using format DD/MM/YYYY: ")  # prompting user for re-entry
                date_search = data[(data['Date'] == search)]
            else:
                print("\n\t\t:: User Logs by Date ::")
                print("-" * 42)
                print("   There are", len(date_search), "User Logs for this Date\n")  # printing length of date_search
                print(date_search.to_string(index=False))  # converting to string so print output looks presentable

        elif extract_data_selection == "3":
            cols = ["Name", "Date"]  # list usage for req 7 list requirement
            data = pd.read_csv('data.txt', sep=',', header=None, names=cols)  # pulling list cols into names
            user_login_dates = pd.unique(data["Name"])  # unique names placed in user_login_dates
            names_and_dates = {key: [] for key in user_login_dates}  # unique names placed into dict as keys

            for key in names_and_dates:
                names = data.loc[data["Name"] == key]  # getting records for a specific group
                names_and_dates[key] = set(names["Date"])  # set usage for req 7 list requirement

            print("\n\t   :: View Records by User ::")
            print("-" * 42)
            for key in names_and_dates:  # for loop that prints out dictionary keys(names) and then the values(dates)
                print("\t\t  Name:", key)
                for values in names_and_dates[key]:
                    print("\t\t\t", values)
                print()

        elif extract_data_selection == "4":
            cols = ["Name", "Date"]  # use of list to satisfy list requirement
            data = pd.read_csv('data.txt', sep=',', header=None, names=cols)  # pulling cols list into names
            print("\n\t   :: Count of User Logins ::")
            print("-" * 42)
            names = data["Name"].value_counts()   # counts all instances of different values in Name column
            names = names.to_dict()  # initialising dict

            for key, value in names.items():  # for loop for dictionary to print keys(names) and login numbers(values)
                print("  ", key, "has logged in", value, "times")

        elif extract_data_selection == "5":
            print("\n\t\t  Exiting to Main Menu")
            extract_data_loop = False

        else:
            print("\nThere is no menu", extract_data_selection, "please try again")  # entry exception handling


def chat_application():  # Section D req 9 & 10
    chat_application_loop = True
    while chat_application_loop:
        print("\n\t\t :: Chat Application ::")  # Menu
        print("-" * 42)
        print("1. Start Server")
        print("2. Start Chat (Client)")
        print("3. Return to Main Menu\n")

        chat_application_selection = input("Select a menu - Input a number: ")
        while not chat_application_selection.isdigit():  # digit exception handling
            chat_application_selection = input("\nYou have entered a non digit value, Select again: ")

        if chat_application_selection == "1":
            print("\nStarting Server")
            os.system("start cmd /k python server.py")  # calling os library to start the server.py file

        elif chat_application_selection == "2":
            print("\n Opening Chat Client")
            os.system("start cmd /k python client.py")  # calling os library to start the client.py file

        elif chat_application_selection == "3":
            print("\n\t\t  Exiting to Main Menu")
            chat_application_loop = False  # breaking out of submenu loop returning to main menu

        else:
            print("\nThere is no menu", chat_application_selection, "please try again")  # entry exception handling


# This is the main while loop that checks for correct input from the user for the menu and then based on input navigates
# around the program or exits.
main_loop = True
while main_loop:
    print("\n\t:: Welcome to the Application ::")
    print("-" * 42)
    print("1: Encrypt Data")
    print("2: Extract information from files")
    print("3: Chat Application")
    print("4: Quit\n")
    main_selection = input("Select a menu - Input a number: ")  # asking user for menu input
    while not main_selection.isdigit():  # checking that main menu selection is a digit
        main_selection = input("\nYou have entered a non digit value, Select again: ")  # prompting reentry

    if main_selection == "1":  # data encryption code block
        encrypt_data()  # calling the encrypt data function which holds all of the code for this block

    elif main_selection == "2":  # data extraction code block
        extract_data()  # calling the extract data function which holds all of the code for this block

    elif main_selection == "3":  # chat application code block
        chat_application()  # calling the chat application function which holds all of the code for this block

    elif main_selection == "4":  # quits out of the program
        print("\nYou have exited the Application")
        quit()

    else:  # catches incorrect digit input
        print("\nThere is no menu", main_selection, "please try again.")


