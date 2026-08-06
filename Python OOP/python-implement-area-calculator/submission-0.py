import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None):
        if width != None:
            return length * width
        else:
            x = math.pi * length**2
            return round(x,2)

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
