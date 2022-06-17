import string
import random

print("------------------- Password Generator -------------------\n\n")
while True:
    print("[1] Numbers only")
    print("[2] Letters only")
    print("[3] Numbers and Letters only")
    print("[4] Numbers, Letters and Characters")

    option = int(input("\n\nEnter option : "))


    def password_generator1():
        digit = int(input("Enter size of password you want : "))
        characters = list(string.digits)
        random.shuffle(characters)
        password = []

        for i in range(digit):
            password.append(random.choice(characters))

        random.shuffle(password)
        print("Your password is : ", "".join(password))


    def password_generator2():
        digit = int(input("Enter size of password you want : "))
        characters = list(string.ascii_letters)
        random.shuffle(characters)
        password = []

        for i in range(digit):
            password.append(random.choice(characters))

        random.shuffle(password)
        print("Your password is : ", "".join(password))


    def password_generator3():
        digit = int(input("Enter size of password you want : "))
        characters = list(string.ascii_letters + string.digits)
        random.shuffle(characters)
        password = []

        for i in range(digit):
            password.append(random.choice(characters))

        random.shuffle(password)
        print("Your password is : ", "".join(password))


    def password_generator4():
        digit = int(input("Enter size of password you want : "))
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        random.shuffle(characters)
        password = []

        for i in range(digit):
            password.append(random.choice(characters))

        random.shuffle(password)
        print("Your password is : ", "".join(password))


    if option == 1:
        password_generator1()
        break
    elif option == 2:
        password_generator2()
        break
    elif option == 3:
        password_generator3()
        break
    elif option == 4:
        password_generator4()
        break
    else:
        print("\nInvalid Option!  Try again...\n")
