import random
import string

pwd = {}


def password_generator(length):
    lower_characters = string.ascii_lowercase
    upper_characters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = lower_characters + upper_characters
    + numbers + special_characters

    password = "".join(random.sample(all_characters, length))

    return password


def generate_password():
    print("generating new credential...")

    app_name = input("Enter the name of the app: ")
    username = input("Enter the username for this app: ")

    pwd_length = int(input("Enter the length of the password: "))

    password = password_generator(pwd_length)

    global pwd

    try:
        pwd[app_name] = {"username": username, "password": password}
        print("New credentials created for " + app_name)

    except:
        print("There was an error generating the credential...")


def modify_password():
    print("modifying existing password...")
    # app_name = input("enter app name: ")
    # username = input("Enter the username for this app: ")
    # global pwd


def delete_password():
    print("deleting existing credential...")
    app_name = input("enter app name: ")

    global pwd

    try:
        del pwd[app_name]
        print("Credentials deleted for " + app_name)
    except:
        print("No credential for " + app_name)


def retrieve_password():
    print("retrieving existing credential...")
    app_name = input("enter app name: ")
    global pwd

    try:
        print(pwd[app_name])
    except:
        print("No credential for " + app_name)


while True:
    print("Welcome to Password Manager")

    print("")
    print("1. Generate Password")
    print("2. Modify Password")
    print("3. Delete Password")
    print("4. Retrieve Password")

    option = input("Select your option: ")

    if option == "1":
        generate_password()

    elif option == "2":
        modify_password()

    elif option == "3":
        delete_password()

    elif option == "4":
        retrieve_password()

    else:
        print("Invalid option selected.")

    again = input("Do you want to continue? y or n: ")
    again = again.lower()

    if again == 'y':
        continue

    else:
        print("thank you for using the password manager app...")
        break
