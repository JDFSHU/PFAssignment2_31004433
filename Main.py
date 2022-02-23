import random
import string
import socket
from threading import Thread

# Name: Jacob Frazer
# Student Number: 31004433
# Computer Networks


def main_menu():  # Main menu function
    print("\n:: Welcome to the Application ::")
    print("=" * 32)
    print("1: Encrypt Data")
    print("2: Extract information from files")
    print("3: Chat Application")
    print("4: Quit\n")


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):  # Encrypt uppercase characters
            result += chr((ord(char) + s - 65) % 26 + 65)
        if (char.isspace()):  # ensuring whitespace / space
            result += chr((ord(char)))
        else: # Encrypt lowercase characters
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def encrypt_data():
    encrypt_data_loop = True
    while encrypt_data_loop:
        print("\n:: Encrypt Data ::")
        print("1. Encrypt a message and save into a file")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Return to Main Menu\n")

        encrypt_data_selection = input("Select a menu - Input a number: ")
        while not encrypt_data_selection.isdigit():  # checking that main menu selection is a digit
            encrypt_data_selection = input("\nYou have entered a non digit value, Select again: ")

        if encrypt_data_selection == "1":
            message_to_encrypt = input("Input a message to encrypt: ")  # allows user to input a message
            print("Your message is ", message_to_encrypt)  # user prompted with their message
            encryption_key = int(input(
                "Input a number for the encryption key (number should be between 1 and 26 - inclusive: "))
            print("Your encryption key is: ", encryption_key)
            print("Encoded Message: " + encrypt(message_to_encrypt, encryption_key))
            print("\nMessage saved to encoded_msg.txt")
            with open("encoded_msg.txt", "w") as f:
                f.write(encrypt(message_to_encrypt, encryption_key))

        elif encrypt_data_selection == "2":
            print("option 2 test")

        elif encrypt_data_selection == "3":
            print("option 3 test")

        elif encrypt_data_selection == "4":
            print("\n Exiting to Main Menu")
            encrypt_data_loop = False

        else:
            print("\nThere is no menu", encrypt_data_selection, "please try again")


def extract_data():
    print("test")


def chat_application():
    print("test")


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


