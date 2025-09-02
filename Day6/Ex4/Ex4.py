class InvalidLengthError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass

def validate_username(username):
    if not (5 <= len(username) <= 15):
        raise InvalidLengthError("Username must be between 5 and 15 characters.")
    if not username.isalnum():
        raise InvalidCharacterError("Username must contain only alphanumeric characters.")

def register_user(filename):
    try:
        username = input("Enter a username to register: ").strip()
        validate_username(username)

        with open(filename, 'a') as file:
            file.write(username + '\n')
        print(f"Username '{username}' registered successfully!")

    except InvalidLengthError as e:
        print(f"InvalidLengthError: {e}")
    except InvalidCharacterError as e:
        print(f"InvalidCharacterError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Registration attempt complete.")

register_user("users.txt")
