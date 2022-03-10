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

    def encrypt(text, s):  # indented function for returning Caesar cipher encryption
        result = ""
        whitespace = "@"  # white space / spaces encrypted as @ symbol
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):  # Encrypt uppercase characters
                result += chr((ord(char) + s - 65) % 26 + 65)
            if (char.isspace()):  # ensuring whitespace / space is included in encryption
                result += chr((ord(whitespace)))
            else:  # Encrypt lowercase characters
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    def decrypt(text, s):  # indented function for returning Caesar cipher encryption
        result = ""
        whitespace = " "  # white space / spaces encrypted as @ symbol
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):  # Encrypt uppercase characters
                result += chr((ord(char) - s - 65) % 26 + 65)
            if (char.isspace()):  # ensuring whitespace / space is included in encryption
                result += chr((ord(whitespace)))
            else:  # Encrypt lowercase characters
                result += chr((ord(char) - s - 97) % 26 + 97)
        return result

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
            encryption_key = int(input(
                "\nInput a number for the encryption key (number should be between 1 and 26 - inclusive: "))
            print("Your encryption key is: ", encryption_key)
            print("Encoded Message: " + encrypt(message_to_encrypt, encryption_key))
            print("\nMessage saved to encoded_msg.txt")
            with open("encoded_msg.txt", "w") as f:  # file handing with open allows me to not need a close statement
                f.write(encrypt(message_to_encrypt, encryption_key))

        elif encrypt_data_selection == "2":  # req 3
            file_input = input("Please input the file name to encrypt (format filename.txt): ")
            with open(file_input) as file_data:
                lines = file_data.read().strip()
                print(lines)
            file_encryption_key = int(input("\nPlease enter the key to encrypt the message: "))
            with open("encryptedFile.txt",
                      "w") as new_encrypted_file:  # file handing with open allows me to not need a close statement
                new_encrypted_file.write(encrypt(lines, file_encryption_key))
            print("Encryption applied, file saved as encryptedFile.txt ")
            with open("encryptedFile.txt", "r") as show_file:
                lines = show_file.read()
                print(lines)

        elif encrypt_data_selection == "3":  # req 4
            print("option 3 test")

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
            cols = ["\b: Names :", ": Date :"]  # defining the columns
            data = pd.read_csv('data.txt', sep=",", names=cols, )  # adds column header
            data.index += 1  # increments index position so index doesnt start at 0
            data.index.names = ["No"]  # index position header
            print(f"\n\t:: View ALl Records :: \n "
                  f"\b\b--------------------------------\n\n", data)
            print()
            print("-" * 33)

        elif extract_data_selection == "2":
            print("option 2 test")

        elif extract_data_selection == "3":
            print("option 3 test")

        elif extract_data_selection == "4":
            print("option 4 test")

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


