class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()  # Normalize the operation string

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                return "Error: Division by zero is undefined."
            return self.a / self.b
        else:
            return "Error: Unsupported operation."


# Example usage:
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

calc = Calculator(a, b, operation)
result = calc.calculate()

print("Result:", result)
