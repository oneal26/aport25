import random
import string 


# generates single password randomly with certain criteria 
def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):

    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation 
    
    if not characters:
        return "Error: Character types not selected."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# main function to handle user interaction & password generation 
def main():
    while True: 
        try: 
            num_password = int(input("How many passwords do you want genertaed? "))
            if num_password <= 0:
                print("Please enter a positive number of passwords.")
                continue
            break
        except ValueError:
            print ("Invalid input. Please enter a number.")
    
    while True:
        try: 
            password_length = int(input("Enter desired password length: "))
            if password_length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError: 
            print("Invalid input. Enter a number.")

    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    for i in range(num_password):
        password = generate_password(password_length, use_lowercase, use_uppercase, use_digits, use_symbols)
        if "Error" in password: 
            print(f"Password {i+1}: {password}")
            break 
        print(f"Password {i+1}: {password}")


if __name__ == "__main__":
    main()