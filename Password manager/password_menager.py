import os
# TODO: Add decryption and encryption.
def master_password_set():
    with open("master.txt", "w") as f:
        f.write(input("Set your master password: "))

def master_password_ask(password):
    with open("master.txt", "r") as f:
        stored_password = f.read().strip()
    return password == stored_password

def start_program():
    return input("Do you want to start the program? (yes/no): ").lower() == "yes"

def first_time():
    path = "master.txt"
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        master_password_set()
    else:
        password = input("What is your master password: ")
        if not master_password_ask(password):
            print("Incorrect password!")
            exit()

def see_all():
    path = "passwords.txt"
    if not os.path.exists(path):
        print("This is your database:")
        print("No passwords stored yet.")
        return
    with open(path, "r") as f:
        print("This is your database:")
        print(f.read())

def add_password():
    pass_ad = input("What is the password you want to add to the database: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{pass_ad}\n")

def main():
    if start_program():
        first_time()
        see_all()
        while input("Do you want to add a password to the database? (yes/no): ").lower() == "yes":
            add_password()
        see_all()
    input("Goodbye! Press Enter to shut down...")

main()
