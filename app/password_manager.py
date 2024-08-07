import os
import sys
from cryptography.fernet import Fernet
import getpass
import subprocess

# Generar una clave y guardarla en un archivo (haz esto solo una vez)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Cargar la clave desde el archivo
def load_key():
    return open("key.key", "rb").read()

# Añadir una contraseña
def add_password(service, password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(service + "|" + encrypted_password.decode() + "\n")

# Recuperar una contraseña
def get_password(service):
    key = load_key()
    f = Fernet(key)
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            service_name, encrypted_password = line.strip().split("|")
            if service_name == service:
                decrypted_password = f.decrypt(encrypted_password.encode()).decode()
                return decrypted_password
    return None

# Eliminar una contraseña
def delete_password(service):
    key = load_key()
    f = Fernet(key)
    lines = []
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
    with open("passwords.txt", "w") as file:
        for line in lines:
            service_name, encrypted_password = line.strip().split("|")
            if service_name != service:
                file.write(line)

def check_sudo():
    if os.geteuid() != 0:
        print("This script requires sudo privileges. Please run it with sudo.")
        # Re-run the script with sudo
        subprocess.call(['sudo', 'python3'] + sys.argv)
        sys.exit()

def main():
    check_sudo()
    print("Password Manager")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Delete Password")
    print("4. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        
        if choice == "1":
            service = input("Enter the service: ")
            password = getpass.getpass("Enter the password: ")
            add_password(service, password)
            print(f"Password for {service} added successfully.")
        
        elif choice == "2":
            service = input("Enter the service: ")
            password = get_password(service)
            if password:
                print(f"The password for {service} is {password}")
            else:
                print(f"No password found for {service}.")
        
        elif choice == "3":
            service = input("Enter the service: ")
            delete_password(service)
            print(f"Password for {service} deleted successfully.")
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Verificar si la clave ya existe, si no, generarla
    if not os.path.exists("key.key"):
        generate_key()
    main()

