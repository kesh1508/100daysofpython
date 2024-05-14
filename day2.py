# calculator.py

class Calculator:
    def __init__(self):
        self.__history = []  # Encapsulation: private attribute to store history

    def add(self, a, b):
        result = a + b
        self.__history.append(f"add({a}, {b}) = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.__history.append(f"subtract({a}, {b}) = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.__history.append(f"multiply({a}, {b}) = {result}")
        return result

    def divide(self, a, b):
        if b != 0:
            result = a / b
            self.__history.append(f"divide({a}, {b}) = {result}")
            return result
        else:
            self.__history.append(f"divide({a}, {b}) = Error! Division by zero.")
            return "Error! Division by zero."

    def get_history(self):
        return self.__history

# Inheritance: Creating a ScientificCalculator that extends Calculator
class ScientificCalculator(Calculator):
    def power(self, base, exponent):
        result = base ** exponent
        self._Calculator__history.append(f"power({base}, {exponent}) = {result}")
        return result

    def square_root(self, number):
        if number >= 0:
            result = number ** 0.5
            self._Calculator__history.append(f"square_root({number}) = {result}")
            return result
        else:
            self._Calculator__history.append(f"square_root({number}) = Error! Negative number.")
            return "Error! Negative number."
###########################################################################################################################################
# main.py

from calculator import Calculator, ScientificCalculator

# Create an instance of Calculator
calc = Calculator()

# Performing basic operations
print("Addition: 5 + 3 =", calc.add(5, 3))           # Output: 8
print("Subtraction: 5 - 3 =", calc.subtract(5, 3))   # Output: 2
print("Multiplication: 5 * 3 =", calc.multiply(5, 3)) # Output: 15
print("Division: 5 / 3 =", calc.divide(5, 3))         # Output: 1.666...
print("Division by zero: 5 / 0 =", calc.divide(5, 0)) # Output: Error! Division by zero.

# Accessing the history (encapsulation)
print("\nHistory of operations:")
for entry in calc.get_history():
    print(entry)

# Create an instance of ScientificCalculator
sci_calc = ScientificCalculator()

# Performing scientific operations
print("\nPower: 2^3 =", sci_calc.power(2, 3))           # Output: 8
print("Square Root: 16 =", sci_calc.square_root(16))    # Output: 4.0
print("Square Root of negative number: -4 =", sci_calc.square_root(-4)) # Output: Error! Negative number.

# Accessing the history (including inherited methods)
print("\nHistory of operations (scientific calculator):")
for entry in sci_calc.get_history():
    print(entry)
