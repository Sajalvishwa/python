class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))