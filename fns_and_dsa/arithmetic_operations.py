def perform_operation(num1, num2, operation):
    if operation == "multiply":
        return num1 * num2
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        if num1 or num2 == 0:
            print("Division by zero isn't allowed")
        else:
            num1 / num2