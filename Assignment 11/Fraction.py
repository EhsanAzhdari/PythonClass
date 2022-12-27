class Fraction:
    def __init__(self, numerator, denominator):
        # Class properties
        self.numerator = numerator
        self.denominator = denominator
        

    # Class methods
    def sum(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        result = Fraction(numerator, denominator)
        return result
    
    def sub(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        result = Fraction(numerator, denominator)
        return result

    def mul(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        result = Fraction(numerator, denominator)
        return result

    def div(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        result = Fraction(numerator, denominator)
        return result
        
    def convert_Fraction_to_Number(self):
        result = self.numerator / self.denominator
        return result
    
    def simplification(self):
        if self.numerator < self.denominator:
            min = self.numerator
        elif self.numerator > self.denominator:
            min = self.denominator
        else:
            return Fraction(1, 1)
        
        while True:
            if self.numerator % min == 0 and self.denominator % min ==0:
                numerator = self.numerator // min
                denominator = self.denominator // min
                result = Fraction(numerator, denominator)
                return result
            min -= 1
    
    def show(self):
        print(self.numerator, "/", self.denominator)