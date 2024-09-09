class Calculator:
    def add(self, a, b):
        if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
            raise TypeError("Custom Error: Inputs must be numeric")
        return a + b