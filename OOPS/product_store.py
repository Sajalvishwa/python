class product :
    count = 0
    def __init__(self , name , price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name} costs {self.price}"
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def discount(price , percentage):
        return price - (price * percentage / 100)

laptop = product("Laptop" , 1000)
print(laptop.get_info())
print(product.get_count())