def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
    except ZeroDivisionError as e:
        return "Erro: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        result = numerator / denominator
        print(f"{result}")

