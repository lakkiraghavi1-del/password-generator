import random
import string

def generate_password(length):
    if length < 4:
        return None
      
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = string.punctuation
  
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(special)
    ]

    
    all_characters = lowercase + uppercase + numbers + special

    for i in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)
  
while True:

    print("\n======================================")
    print("       PASSWORD GENERATOR")
    print("======================================")
    print("1. Generate Password")
    print("2. Generate Multiple Passwords")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    
    if choice == "1":

        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length must be at least 4.")
            else:
                password = generate_password(length)

                print("\nGenerated Password:")
                print(password)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":

        try:
            length = int(input("Enter password length: "))
            count = int(input("How many passwords do you want? "))

            if length < 4:
                print("Password length must be at least 4.")

            elif count <= 0:
                print("Number of passwords must be greater than 0.")

            else:
                print("\nGenerated Passwords:")

                for i in range(count):
                    password = generate_password(length)
                    print(str(i + 1) + ".", password)

        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "3":
        print("\nThank you for using Password Generator!")
        break

    # Invalid choice
    else:
        print("\nInvalid choice! Please select 1, 2, or 3.")
            
