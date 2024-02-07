class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self,bark):
        print(bark)

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)
dog2=Dog("puppy", 2)
print(my_dog.name)
print(dog2.name)
my_dog.sound("bark")
class Computer:
    def programs (self, Language, make, brand) :
        
        print(Language,brand,make)

Computer1=Computer()
Computer1.programs("Make","brand","Hp")


class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Encapsulation using underscore

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
print(account.get_balance())

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Purr!"

my_dog = Dog()
print(my_dog.speak())  # Outputs: Woof!
my_cat= Cat()
print(my_cat.speak())

class Robot:
    def move_left(self):
        return "Moved Left"
    def move_right(self):
        return "Moved Right"
    
my_robot=Robot()
print(my_robot.move_left())
print(my_robot.move_right())

class Minirobot(Robot):
    pass
my_minirobot=Minirobot() 
print(my_minirobot.move_left())
print(my_minirobot.move_right())
# When inheritance takes place there's no need to repeat the def function.