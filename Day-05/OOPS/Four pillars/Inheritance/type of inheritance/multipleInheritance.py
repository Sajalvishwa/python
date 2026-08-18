# Multiple Inheritance
# One child class inherits from multiple parent classes

class Father:

    def work(self):
        print("Father is working")


class Mother:

    def cook(self):
        print("Mother is cooking")


class Child(Father, Mother):
    pass


child = Child()

child.work()   # From Father
child.cook()   # From Mother