class ComplexNumber:
    def __init__(self, real, image):
        # Class properties
        self.real = real
        self.image = image
    
    # Class methods
    def show(self):
        print(f"{self.real} + i{self.image}")
        
    def sum(self, other):
        real = self.real + other.real
        image = self.image + other.image
        result = ComplexNumber(real, image)
        return result
        
    def sub(self, other):
        real = self.real - other.real
        image = self.image - other.image
        result = ComplexNumber(real, image)
        return result
    
    def mul(self, other):
        real = self.real * other.real - self.image * other.image
        image = self.real * other.image + self.image *other.real
        result = ComplexNumber(real, image)
        return result