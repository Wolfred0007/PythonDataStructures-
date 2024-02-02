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
  