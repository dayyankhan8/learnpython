def calculate_expression(x, operator, z):
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        return x / z

def main():
    expression = input("Please enter an arithmetic expression (e.g., x + y): ")
    x, operator, z = expression.split()

    x = int(x)
    z = int(z)

    result = calculate_expression(x, operator, z)
    print(f"Result: {result}")

main()