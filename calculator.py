def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a % b

def floor_division(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a // b


while True:
    print("\n========== SIMPLE CALCULATOR ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Floor Division (//)")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "7":
        print("Thank you for using the Calculator!")
        break

    elif choice in ["1", "2", "3", "4", "5", "6"]:

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "1":
            print("Result =", add(num1, num2))

        elif choice == "2":
            print("Result =", subtract(num1, num2))

        elif choice == "3":
            print("Result =", multiply(num1, num2))

        elif choice == "4":
            print("Result =", divide(num1, num2))

        elif choice == "5":
            print("Result =", modulus(num1, num2))

        elif choice == "6":
            print("Result =", floor_division(num1, num2))

    else:
        print("Invalid Choice! Please enter a number between 1 and 7.")
        