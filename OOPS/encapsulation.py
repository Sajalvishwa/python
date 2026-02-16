class account :
    def __init__(self,name , id , balance):
        self.name = name #public attribute
        self._id = id #protected attribute
        self.__balance = balance #private attribute

    def get_info(self):
        return f"Account holder: {self.name}, ID: {self._id}, Balance: {self.__balance}"
    
    def set_balance(self , amount):
        if amount >= 0:
            self.__balance = amount
        else:            print("Balance cannot be negative")

acc = account("John Doe" , "12345" , 1000)
print(acc.get_info())