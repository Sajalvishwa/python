from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        return "Woof!"
class cat(animal):
    def sound(self):
        return "Meow!"
dog1 = dog()
cat1 = cat()