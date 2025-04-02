class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance  
    
    def isValid(self, account):
        return 1 <= account <= len(self.accounts) 

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.isValid(account1) and self.isValid(account2) and self.accounts[account1 - 1] >= money:
            self.accounts[account1 - 1] -= money 
            self.accounts[account2 - 1] += money 
            return True 
        return False 

    def deposit(self, account: int, money: int) -> bool:
        if self.isValid(account):
            self.accounts[account - 1] += money 
            return True 
        return False 

    def withdraw(self, account: int, money: int) -> bool:
        if self.isValid(account) and self.accounts[account - 1] >= money:
                self.accounts[account - 1] -= money 
                return True 
        
        return False 


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)