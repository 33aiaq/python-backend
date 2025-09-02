import re

def is_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*]', password):
        return False, "Password must contain at least one special character (!@#$%^&*)."
    return True, ""

def check_passwords(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            passwords = infile.readlines()

        with open(output_file, 'w') as outfile:
            for line_number, pwd in enumerate(passwords, start=1):
                password = pwd.strip()
                if not password:
                    continue
                valid, message = is_strong_password(password)
                if valid:
                    outfile.write(password + '\n')
                else:
                    print(f"Line {line_number}: '{password}' rejected - {message}")

        print(f"Password strength check complete. Strong passwords saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

check_passwords("passwords.txt", "strong_passwords.txt")
