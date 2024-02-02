import json
import getpass


def create_user(username=None):
    user = read_json()
    if username == None:
        username = input("Username: ")
        while username in user:
            print("Username exists, please set a new username.")
            username = input("Username: ")
    else:
        print("Enter new password.")
    password = hash(getpass.getpass('Password: '))
    verpassword = hash(getpass.getpass('Verify Password: '))
    while password != verpassword:
        print("Invalid Password")
        password = hash(getpass.getpass('Password: '))
        verpassword = hash(getpass.getpass('Verify Password: '))
    secret = input("What is your favourite thing in the world: ")
    user[username] = [password, secret]
    user_json = json.dumps(user, indent=3)
    with open("password.json", "w") as outfile:
        outfile.write(user_json)

def login():
    user = read_json()
    username = input("Username: ")
    while username not in user:
        if input("User doesn't exists, press [enter] to try again or any key to create user: ") != "":
            create_user()
            return
        username = input("Username: ")
    password = hash(getpass.getpass('Password: '))
    while password != user[username][0]:
        choice = input("Password incorrect, press [enter] to try again or any key to reset password: ")
        if choice != "":
            key = input("Please enter your favourite thing in the world: ")
            if key == user[username][1]:
                create_user(username)
            else:
                print("Incorrect.")
            return
        else:
            password = hash(getpass.getpass('Password: '))
        
def read_json():
    try:
        with open('password.json', 'r') as openfile:
            return json.load(openfile)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

def menu():
    choice = input("Hello, world!\n1. Login\n2. Register\n").strip()
    if choice == "1":
        login()
    elif choice == "2":
        create_user()
    else:
        print("Invalid choice.")
        
 

menu()


