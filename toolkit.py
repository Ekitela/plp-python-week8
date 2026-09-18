print("Welcome to my Personal Mini-Toolkit!")


# Performs basic arithmetic calculations using two numbers.
def calculator():
    print("\n===== SIMPLE CALCULATOR =====")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator.")


# Allows the user to add, remove, and view items in a to-do list.
def todo_list():
    items = []

    while True:
        print("\nMenu: add / remove / show / done")
        choice = input("What would you like to do? ").lower()

        if choice == "add":
            item = input("Enter an item to add: ")
            items.append(item)
            print(f"{item} added to your list.")

        elif choice == "remove":
            item = input("Enter an item to remove: ")

            if item in items:
                items.remove(item)
                print(f"{item} removed from your list.")
            else:
                print("That item is not on your list.")

        elif choice == "show":
            if items:
                print("Your list:")
                for item in items:
                    print(f"- {item}")
            else:
                print("Your list is empty.")

        elif choice == "done":
            print("Leaving To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


# Checks whether a number is positive, negative, zero, even, or odd.
def number_checker():
    print("\n===== NUMBER CHECKER =====")
    number = int(input("Enter a number: "))

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


# Counts down from a user-provided number to 1.
def countdown():
    print("\n===== COUNTDOWN =====")
    number = int(input("Enter a number to count down from: "))

    for i in range(number, 0, -1):
        print(i)

    print("Countdown complete!")


while True:
    print("\n===== PERSONAL MINI-TOOLKIT =====")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Countdown")
    print("5. Quit")

    choice = input("What would you like to use? ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        number_checker()

    elif choice == "4":
        countdown()

    elif choice == "5":
        print("Thank you for using my Personal Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please choose 1 to 5.")