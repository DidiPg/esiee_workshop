class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner           
        self._balance = balance      
        self.__pin = "1234"          

    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("positif number")

   
    def withdraw(self, amount):
        if amount <= 0:
            print("positif number")
        elif amount <= self._balance:
            self._balance -= amount
        else:
            print("You don't havec enough monye")



        print(f"Count : {self._balance} €")


    def __check_pin(self):
        print("Verication of your code")


if __name__ == "__main__":
    compte = BankAccount("John", 100)
    compte.deposit(50)
    compte.withdraw(30) 

 
    print(compte.owner)      
    print(compte._balance)   
    print(compte._BankAccount__pin)  
