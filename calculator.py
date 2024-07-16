# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a / b

# Display the menu and get user input
print("Select operation:")
print("1. Divide")
print("2. Multiply")
print("3. Add")
print("4. Subtract")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

# Check if choice is one of the four options
if choice in ['1', '2', '3', '4']:
    # Prompt the user to enter two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the corresponding operation based on the user's choice
    if choice == '3':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '4':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '2':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '1':
        print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
