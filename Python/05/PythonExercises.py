# Day 5: Python Function Exercises - Object-Oriented Programming

# 1. Basic class with attributes and method
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

# 2. Inheritance example
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"

# 3. Encapsulation example
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

# 4. Polymorphism example
class Bird:
    def make_sound(self):
        return "Chirp"

class Duck(Bird):
    def make_sound(self):
        return "Quack"

def animal_sound(animal):
    return animal.make_sound()

# 5. Class method and static method
class MathOperations:
    pi = 3.14159

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius * radius

    @staticmethod
    def add(x, y):
        return x + y

# 6. Property decorator
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9


# Example Tests
if __name__ == "__main__":
    dog = Dog("Buddy", "Labrador")
    print(dog.speak())

    cat = Cat("Whiskers")
    print(cat.make_sound())

    account = BankAccount("Eric", 100)
    print("Deposit:", account.deposit(50))
    print("Withdraw:", account.withdraw(30))
    print("Balance:", account.get_balance())

    print("Animal sound (Duck):", animal_sound(Duck()))

    print("Circle area:", MathOperations.circle_area(5))
    print("Addition:", MathOperations.add(3, 4))

    temp = Temperature(0)
    print("Fahrenheit:", temp.fahrenheit)
    temp.fahrenheit = 212
    print("Celsius after setting Fahrenheit to 212:", temp._celsius)
