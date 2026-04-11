"""Python Fundamentals 2025: Домашнее задание 38

Банковский счёт
Создайте класс BankAccount, описывающий банковский счёт.
Объект должен хранить имя владельца и текущий баланс.
Реализуйте методы:
пополнение счёта
снятие средств
отображение баланса
При попытке снять больше, чем есть на счёте, операция не должна выполняться.
Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми."""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.validate_amount(balance)
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.validate_amount(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self.validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Not enough funds.")
        self.__balance -= amount

    @staticmethod
    def validate_amount(amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")

    @property
    def balance(self):
        return self.__balance


    def show_balance(self):
        print(f"Current balance: {self.__balance}")

acc = BankAccount("Alice")
acc.deposit(150)
acc.show_balance()
print(acc.balance)
try:
    acc.deposit(-50)
except ValueError as e:
    print("Error:", e)
acc.show_balance()

try:
    acc.withdraw(200)
except ValueError as e:
    print("Error:", e)
acc.show_balance()

"""История операций
Доработайте класс BankAccount.
Каждая операция пополнения и снятия должна сохраняться в историю.
История должна быть доступна через property history только для чтения.
История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.)."""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.validate_amount(balance)
        self.__owner = owner
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        self.validate_amount(amount)
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        self.validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Not enough funds.")
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    @staticmethod
    def validate_amount(amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        # return self.__history
        # return iter(self.__history)
        return list(self.__history)

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

acc = BankAccount("Alice")
acc.deposit(150)
acc.show_balance()
print(acc.balance)
try:
    acc.deposit(-50)
except ValueError as e:
    print("Error:", e)
acc.show_balance()

try:
    acc.withdraw(30)
    acc.withdraw(200)
except ValueError as e:
    print("Error:", e)
acc.show_balance()

acc.history.append("New operation")

print("Operation history:")
for op in acc.history:
    print("\t", op)