import os

ACCOUNTS_FILE = "accounts.txt"


def save_user_to_file(name, pin):
    with open(ACCOUNTS_FILE, "a") as file:
        file.write(f"{name}|{pin}\n")


def load_users_from_file():
    users = {}
    if not os.path.exists(ACCOUNTS_FILE):
        return users

    with open(ACCOUNTS_FILE, "r") as file:
        for line in file:
            name, pin = line.strip().split("|")
            users[name] = pin
    return users
