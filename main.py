def main():
    print("Simple Calculator")

    # Input first number
    num1 = float(input("Enter first number: "))

    # Input second number
    num2 = float(input("Enter second number: "))

    # Input operation
    print("Choose the operation to perform:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    operation = input("Select an option (1, 2, 3, or 4): ")

    # Perform calculation
    if operation == '1':
        result = num1 + num2
        symbol = '+'
    elif operation == '2':
        result = num1 - num2
        symbol = '-'
    elif operation == '3':
        result = num1 * num2
        symbol = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        symbol = '/'
    else:
        print("Invalid input. Please choose a valid operation.")
        return

    # Output the result
    print(f"{num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
    main()


