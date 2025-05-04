class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Create an object of the Dog class
d = Dog()
d.sound()