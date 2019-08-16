
class Numbers:
    def __init__(self):  # Class Constructor
        pass

    def add(self, number1, number2):  # Method Add: adding two numbers.
        result = number1 + number2    # performing Add operation
        return result

    def subtract(self, number1, number2):  # Method Subtract: subtracting two numbers.
        result = number1 - number2  # performing Subtract operation
        return result

    def multiply(self, number1, number2):  # Method Multiply: multiplying two numbers.
        result = number1 * number2  # performing Multiply operation
        return result

    def division(self, number1, number2):  # Method Division: dividing two numbers.
        result = number1 / number2  # performing Division operation
        return result


class Vectors:
    def __init__(self):
        pass

    def add(self, vector1, vector2, size):  # Method Add: adding two vectors.
        for i in range(size):
            print(vector1[i], "+", vector2[i], "=", vector1[i] + vector2[i])

    def subtract(self, vector1, vector2, size):  # Method Add: adding two vectors.
        for i in range(size):
            print(vector1[i], "-", vector2[i], "=", vector1[i] - vector2[i])

    def multiply(self, vector1, vector2, size):  # Method Add: adding two vectors.
        for i in range(size):
            print(vector1[i], "*", vector2[i], "=", vector1[i] * vector2[i])

    def division(self, vector1, vector2, size):  # Method Add: adding two vectors.
        for i in range(size):
            print(vector1[i], "/", vector2[i], "=", vector1[i] / vector2[i])
