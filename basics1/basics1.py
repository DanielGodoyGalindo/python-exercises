from datetime import datetime


# Exercise 1
def welcome():
    print("Hello, world!")


# welcome()


# Exercise 2
def greeting():
    name = ""
    valid = False
    while not valid:
        name = input("Please, enter your name:")
        if not name.isnumeric():
            valid = True
    print("Hello, " + name)


# greeting()


# Exercise 3
def sum_numbers():
    valid = False
    while not valid:
        num1 = input("Please enter the first number:")
        num2 = input("Please enter the second number:")
        if not num1.isnumeric() or not num2.isnumeric():
            print("One of the numbers is not numeric! Try again")
        else:
            valid = True
    print(int(num1) + int(num2))


# sum_numbers()


# Exercise 4
def meters2cm() -> None:
    valid = False
    while not valid:
        meters = input("Please enter the number of meters:")
        if not meters.isnumeric():
            print("The value has to be a number!")
        else:
            meters = int(meters)
            centimeters = meters * 100
            valid = True
    print(f"{meters} meters are {centimeters} centimeters")


# meters2cm()


# Exercise 5
def calc_age():
    current_year = datetime.now().year
    valid = False
    while not valid:
        birth_year = input("What is you year of birth? ")
        if not birth_year.isnumeric():
            print("The year is not a number! Try again.")
        else:
            valid = True
    print(f"Your age should be {current_year - int(birth_year)}")


# calc_age()


# Exercise 6
def even_numbers(start_number: int, end_number: int):
    if end_number < start_number:
        start_number, end_number = end_number, start_number
    for i in range(start_number, end_number):
        if i % 2 == 0:
            print(i)


# even_numbers(1, 20)


#  Exercise 7
def multiplication_table():
    while True:
        number = input("Please, type a number: ")
        if not number.isnumeric():
            print("Only numbers allowed!")
        else:
            number = int(number)
            break
    for i in range(1, 11):
        print(f"{i} x {number} = {i * number}")


# multiplication_table()


# Exercise 8
def countdown():
    for i in range(10, 0, -1):
        print(i)
    print("Blast off!")


# countdown()


# Exercise 9
def secret_password():
    user_input = input("Type the password: ")
    if user_input != "secret123":
        print("Access denied.")
    else:
        print("Welcome.")


# secret_password()


# Exercise 10
def number_type():
    while True:
        try:
            number = float(input("Type a number: "))
            break
        except ValueError:
            print("This is not a number!")
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is zero.")


# number_type()
