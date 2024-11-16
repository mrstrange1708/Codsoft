import random
import string

def generate_password(length):
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")

   
    letters = string.ascii_letters  
    digits = string.digits 
    special_characters = string.punctuation  
    
    mandatory_chars = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

   
    all_characters = letters + digits + special_characters
    remaining_length = length - len(mandatory_chars)
    password_body = random.choices(all_characters, k=remaining_length)

    password = mandatory_chars + password_body
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        secure_password = generate_password(length)
        print(f"Generated Password: {secure_password}")
    except ValueError as e:
        print(f"Error: {e}")