import json
import os

# Define the path to the JSON file where user data will be stored
user_data_file = 'user_data.json'

def save_user_data(data):
    """Save the user data to the JSON file."""
    with open(user_data_file, 'w') as file:
        json.dump(data, file, indent=4)

def load_user_data():
    """Load the user data from the JSON file."""
    if os.path.exists(user_data_file):
        with open(user_data_file, 'r') as file:
            return json.load(file)
    return {}

def sign_up():
    """Sign up a new user."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    mobile_number = input("Enter mobile number: ")

    # Load existing user data
    user_data = load_user_data()

    if username in user_data:
        print("Username already exists. Please try signing in.")
        return

    # Add new user data
    user_data[username] = {
        'password': password,
        'mobile_number': mobile_number
    }

    # Save the updated user data
    save_user_data(user_data)
    print("Sign up successful!")

def sign_in():
    """Sign in an existing user."""
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Load user data
    user_data = load_user_data()

    # Check if the username exists and the password matches
    if username in user_data and user_data[username]['password'] == password:
        print(f"Welcome to the device, {username}!")
        print(f"Your mobile number is: {user_data[username]['mobile_number']}")
    else:
        print("Incorrect credentials. Program terminated.")

def main():
    """Main function to handle the sign up or sign in process."""
    print("Choose an option:")
    print("1. Sign Up")
    print("2. Sign In")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        print("Invalid choice. Please restart the program.")

if __name__ == "__main__":
    main()
