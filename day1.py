# File: calculator.py

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
#######################################################################
# File: main.py

# Import the Calculator class from the calculator module
from calculator import Calculator

def main():
    # Create an instance of the Calculator class
    calc = Calculator()

    # Perform some calculations
    result_add = calc.add(5, 3)
    result_subtract = calc.subtract(10, 4)
    result_multiply = calc.multiply(7, 2)
    result_divide = calc.divide(20, 5)

    # Display the results
    print("Result of addition:", result_add)
    print("Result of subtraction:", result_subtract)
    print("Result of multiplication:", result_multiply)
    print("Result of division:", result_divide)

if __name__ == "__main__":
    main()
#####################################################################
