'''
You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:

The given account number(s) are between 1 and n, and
The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
Implement the Bank class:

Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.
'''

class Bank:
    # validate account 
    def isValidAccount(self, account):
        return 1 <= account <= len(self.accounts)

    def __init__(self, balance: List[int]):
        self.accounts = balance 

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # transfer only if account1 >= money 
        if self.isValidAccount(account1) and self.isValidAccount(account2) and self.accounts[account1 - 1] >= money:
            self.accounts[account1 - 1] -= money 
            self.accounts[account2 - 1] += money 
            return True 
        return False 

    def deposit(self, account: int, money: int) -> bool:
        if self.isValidAccount(account):
            self.accounts[account - 1] += money
            return True 
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.isValidAccount(account) and self.accounts[account - 1] >= money:
            self.accounts[account - 1] -= money
            return True 
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)