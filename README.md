# Password Manager

A simple password manager from terminal that keeps your passwords in a file and encrypts them.

## Dependencies

- Cryptography 
  ``` 
  pip install cryptography 
  ```

## How to Use

### Running Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   sudo python3 app/password_manager.py
   ```

### Using Docker

1. **Build the Docker image**:
   ```bash
   docker build -t password-manager .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -it --rm --name password-manager --privileged password-manager
   ```

## Features

- [x] Encrypts passwords using the `cryptography` library.
- [x] Requires sudo authentication to run.
- [ ] Add a Graphical interface (maybe)
- [ ] Autofill option or something like that
- [ ] Password creation option

## Problems

- [x] You can still delete passwords even if it is not run as sudo. (This issue has been fixed.)

## Project Structure

```
password-manager/
├── .github/
│   └── workflows/
│       └── (GitHub Actions configurations)
├── app/
│   ├── password_manager.py
│   └── key.key (optional, will be generated if not present)
├── tests/
│   └── (test files)
├── README.md
├── requirements.txt
└── Dockerfile
```

## How It Works

### Adding a Password

1. Select the "Add Password" option.
2. Enter the service name.
3. Enter the password.

### Retrieving a Password

1. Select the "Get Password" option.
2. Enter the service name.

### Deleting a Password

1. Select the "Delete Password" option.
2. Enter the service name.

### Notes

- The passwords are stored in an encrypted format in a file named `passwords.txt`.
- The encryption key is stored in a file named `key.key`.
- If `key.key` does not exist, it will be generated automatically.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or new features to add.

## Additional Documentation

* Look in: [Links](https://lacy-period-db7.notion.site/Password-manager-Documentation-76335cb6012d46fc98184a5d74f80820?pvs=4)

