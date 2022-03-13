import pandas as pd
import os


# Name: Jacob Frazer
# Student Number: 31004433
# Computer Networks


def main_menu():  # Main menu function
    print("\n:: Welcome to the Application ::")
    print("-" * 32)
    print("1: Encrypt Data")
    print("2: Extract information from files")
    print("3: Chat Application")
    print("4: Quit\n")


def encrypt_data():  # Section B req 2, 3 & 4

    def encrypt(key, message):
        message = message.lower()  # converting any message to upper
        alpha = "abcdefghijklmnopqrstuvwxyz"  # alphabet used to encrypt
        result = ""  # creating empty variable to store for loop as it iterates

        for letter in message:
            if letter in alpha:  # if the for loop detects a matching letter in alphabet
                letter_index = (alpha.find(letter) + key) % len(
                    alpha)  # finds index position and adds key, modulo prevents looping around the alpha string
                result = result + alpha[letter_index]
            else:
                result = result + letter

        encrypted_message = result.replace(" ", "@")
        encrypted_message = encrypted_message.replace("\n", "!")
        return encrypted_message

    def decrypt(key, message):
        message = message.lower()  # converting any message to upper
        alpha = "abcdefghijklmnopqrstuvwxyz"  # alphabet used to encrypt
        result = ""  # creating empty variable to store for loop as it iterates

        for letter in message:
            if letter in alpha:  # if the for loop detects a matching letter in alphabet
                letter_index = (alpha.find(letter) - key) % len(
                    alpha)  # finds index position and adds key, modulo prevents looping around the alpha string
                result = result + alpha[letter_index]
            else:
                result = result + letter

        decrypted_message = result.replace("@", " ")
        decrypted_message = decrypted_message.replace("!", "\n")
        return decrypted_message

    encrypt_data_loop = True
    while encrypt_data_loop:
        print("\n\t :: Encrypt/Decrypt Data ::")
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
            print("Your message is ", message_to_encrypt)  # user prompted with their message
            while True:
                try:
                    encryption_key = int(input(
                        "\nInput a number for the encryption key between 1 and 26: "))
                    while encryption_key < 1 or encryption_key > 26:
                        encryption_key = int(input(
                            "\nYou're key is out of bounds, please re enter a key between 1 and 26: "))

                    print("Your encryption key is: ", encryption_key)
                    print("Encoded Message: " + encrypt(encryption_key, message_to_encrypt))
                    print("\nMessage saved to encoded_msg.txt")
                    with open("encoded_msg.txt",
                              "w") as f:  # file handing with open allows me to not need a close statement
                        f.write(encrypt(encryption_key, message_to_encrypt))
                    break
                except ValueError:
                    print("You must enter a NUMBER between 1 and 26")

        elif encrypt_data_selection == "2":  # req 3
            while True:
                file_input = input("\nPlease input the file name to encrypt (format filename.txt): ")
                print()
                try:
                    with open(file_input) as file_data:
                        lines = file_data.read().strip()
                        print(lines)
                    break
                except FileNotFoundError:
                    print("File doesn't exist, Check available files or ensure correct input format filename.txt")

            while True:
                try:
                    file_encryption_key = int(input("\nPlease enter the key to encrypt the message: "))
                    while file_encryption_key < 1 or file_encryption_key > 26:
                        file_encryption_key = int(input(
                            "\nYou're key is out of bounds, please re enter a key between 1 and 26: "))
                    with open("encryptedFile.txt",
                              "w") as new_encrypted_file:
                        new_encrypted_file.write(encrypt(file_encryption_key, lines))
                    print("\nEncryption applied, file saved as encryptedFile.txt ")
                    print()
                    with open("encryptedFile.txt", "r") as show_file:
                        lines = show_file.read()
                        print(lines)
                    break
                except ValueError:
                    print("You must enter a NUMBER between 1 and 26")

        elif encrypt_data_selection == "3":  # req 4
            while True:
                file_input = input("\nPlease input the file name to decrypt (format filename.txt): ")
                print()
                try:
                    with open(file_input) as file_data:
                        lines = file_data.read().strip()
                        print(lines)
                    break
                except FileNotFoundError:
                    print("File doesn't exist, Check available files or ensure correct input format filename.txt")

            while True:
                try:
                    file_decryption_key = int(input("\nInput a number for the decryption key between 1 and 26: "))
                    while file_decryption_key < 1 or file_decryption_key > 26:
                        file_decryption_key = int(input(
                            "\nYou're key is out of bounds, please re enter a key between 1 and 26: "))
                    with open("decryptedFile.txt",
                              "w") as new_encrypted_file:
                        new_encrypted_file.write(decrypt(file_decryption_key, lines))
                    print("\nDecryption applied, file saved as decryptedFile.txt \n")
                    with open("decryptedFile.txt", "r") as show_file:
                        lines = show_file.read()
                        print(lines)
                    break
                except ValueError:
                    print("You must enter a NUMBER between 1 and 26")

        elif encrypt_data_selection == "4":
            print("\n Exiting to Main Menu")
            encrypt_data_loop = False

        else:
            print("\nThere is no menu", encrypt_data_selection, "please try again")


def extract_data():  # Section C req 5, 6, 7, & 8
    extract_data_loop = True
    while extract_data_loop:
        print("\n\t:: Extract Data ::")
        print("-" * 28)
        print("1. View all Records")
        print("2. View Records by Date")
        print("3. View Records by User")
        print("4. Count User by Date")
        print("5. Return to Main Menu\n")

        extract_data_selection = input("Select a menu - Input a number: ")
        while not extract_data_selection.isdigit():
            extract_data_selection = input("\nYou have entered a non digit value, Select again: ")

        if extract_data_selection == "1":
            cols = ["\bName", "Date"]  # defining the columns
            data = pd.read_csv("data.txt", sep=",", names=cols)  # adds column header
            data.index += 1  # increments index position so index doesnt start at 0
            data.index.names = ["No"]  # index position header
            print(f"\n\t:: View ALl Records :: \n "
                  f"\b\b--------------------------------\n\n", data)
            print()
            print("-" * 33)

        elif extract_data_selection == "2":
            print("\n:: View Records by Date ::")
            print("-" * 28)
            cols = ["Name", "Date"]  # use of list to satisfy requirement
            data = pd.read_csv("data.txt", header=None, names=cols)
            data.index.names = ["No"]
            data.index += 1
            search = input("\nInput date using format DD/MM/YYYY: ")
            second = data[(data["Date"] == search)]

            while len(second) == 0:
                print("\nNo Record Found! Make sure you are using the correct Date Format: DD/MM/YYYY")
                search = input("\ninput date using format DD/MM/YYYY: ")
                second = data[(data['Date'] == search)]
            else:
                print("\nThere are", len(second), "user logs for this date.\n")
                print(second.to_string(index=False))

        elif extract_data_selection == "3":
            cols = ["Name", "Date"]  # list usage for req 7 list requirement
            data = pd.read_csv('data.txt', sep=',', header=None, names=cols)
            user_login_dates = pd.unique(data["Name"])
            names_and_dates = {key: [] for key in user_login_dates}

            for key in names_and_dates:
                names = data.loc[data["Name"] == key]  # getting records for a specific group
                names_and_dates[key] = set(names["Date"])  # set usage for req 7 list requirement

            print("\n:: View Records by User ::")
            print("-" * 28)
            for key in names_and_dates:
                print("Name:", key)
                for item in names_and_dates[key]:
                    print(item)
                print()

        elif extract_data_selection == "4":
            cols = ["Name", "Date"]  # use of list to satisfy list requirement
            data = pd.read_csv('data.txt', sep=',', header=None, names=cols)
            print("\n\t  :: Count of User Logins ::")
            print("-" * 40)
            names = data["Name"].value_counts()
            names = names.to_dict()  # initialising dict

            for key, value in names.items():  # for loop for dictionary to print keys(names) and logins numbers (values)
                print(key, "has logged in on", value, "occasions.")

        elif extract_data_selection == "5":
            print("\n Exiting to Main Menu")
            extract_data_loop = False
        else:
            print("\nThere is no menu", extract_data_selection, "please try again")


def chat_application():  # Section D req 9 & 10
    chat_application_loop = True
    while chat_application_loop:
        print("\n\t :: Chat Application ::")
        print("=" * 32)
        print("1. Start Server")
        print("2. Start Chat (Client)")
        print("3. Return to Main Menu\n")

        chat_application_selection = input("Select a menu - Input a number: ")
        while not chat_application_selection.isdigit():
            chat_application_selection = input("\nYou have entered a non digit value, Select again: ")
        if chat_application_selection == "1":
            print("\nStarting Server")
            os.system("start cmd /k python server.py")
        elif chat_application_selection == "2":
            print("\n Opening Chat Client")
            os.system("start cmd /k python client.py")
        elif chat_application_selection == "3":
            print("\n Exiting to Main Menu")
            chat_application_loop = False
        else:
            print("\nThere is no menu", chat_application_selection, "please try again")


# This is the main while loop that checks for correct input from the user for the menu and then based on input navigates
# around the program or exits.
main_loop = True
while main_loop:  # loops while main selection isn't expected digits
    main_menu()
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
    else:
        print("\nThere is no menu", main_selection, "please try again.")


