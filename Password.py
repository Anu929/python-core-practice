import random
import string
class WeakPasswordError(Exception):
    pass
def generate_secure_password(length):
    try:
        if not isinstance(length, int):
            raise TypeError("Length must be integer")
        if length < 6:
            raise WeakPasswordError("Password length must be at least 6")
        password=[
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits)
        ]
        remaining=length - 3
        all_chars=string.ascii_letters + string.digits
        password +=random.choices(all_chars,k=remaining)
        random.shuffle(password)
        return ''.join(password)
    except Exception as e:
        return f"Error: {str(e)}"
def main():
    try:
        length=int(input("Enter password length: "))
        result=generate_secure_password(length)
        print("Generated Password:",result)
    except ValueError:
        print("Error: Please enter a valid integer.")
if __name__=="__main__":
    main()