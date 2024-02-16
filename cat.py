#Revmoe pass and complete the cat class
class Cat:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
    def speak(self):
        return 'Meow'

stella = Cat('Stella', 7)
garfield = Cat('Garfield', 50)
#change
stella.speak()
garfield.speak()
#Create objects here
#These should NOT be indented inside the class

