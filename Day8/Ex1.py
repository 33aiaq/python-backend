class Account:
    def __init__(self, acc_no, holder, balance):
        self.acc_no = acc_no
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.holder} ({self.acc_no}): {self.__balance}"

    def __eq__(self, other):
        return isinstance(other, Account) and self.acc_no == other.acc_no



class SavingsAccount(Account):
    def __init__(self, acc_no, holder, balance, interest):
        super().__init__(acc_no, holder, balance)
        self.interest = interest

    def withdraw(self, amount):
        if self.get_balance() - amount >= 100:
            self._Account__balance -= amount


class CheckingAccount(Account):
    def __init__(self, acc_no, holder, balance, overdraft):
        super().__init__(acc_no, holder, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.overdraft:
            self._Account__balance -= amount


s = SavingsAccount("S001", "Lith", 900, 300)
c = CheckingAccount("C001", "Noor", 600, 200)

s.withdraw(450)
s.deposit(100)
s.withdraw(400)

c.withdraw(450)
c.withdraw(100)

print(s)
print(c)

print(c == s)

s2 = SavingsAccount("S001", "Hassan", 1000, 0.03)
print(s == s2)
