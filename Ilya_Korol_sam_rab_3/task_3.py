# Задача №3. Создайте систему управления банковскими счетами, которая позволяет создавать,
# управлять и выполнять операции с банковскими счетами различных клиентов.
# 1)Реализуйте класс Client, представляющий клиента банка. Класс должен иметь атрибуты name (имя клиента) и
# id (уникальный идентификатор клиента).
# 2)Реализуйте класс BankAccount, представляющий банковский счет. Класс должен иметь атрибуты account_number (номер счета),
# balance (баланс счета) и client (объект типа Client, которому принадлежит счет).
# Класс также должен иметь методы deposit(amount) и withdraw(amount), которые позволяют пополнить или снять деньги со счета.
# 3)Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts, который является словарем,
# где ключами являются номера счетов, а значениями - объекты типа BankAccount.
# Класс также должен иметь методы create_account(client, initial_balance) для создания нового счета и
# get_account(account_number) для получения счета по его номеру.
# 4)Добавьте в класс Bank методы для выполнения переводов между счетами (transfer(sender_account, receiver_account, amount)),
# а также для получения общего баланса клиента (get_total_balance(client)), который включает сумму денег на всех его счетах.
# 5)Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег или отсутствие счета при переводе.

class Client:
    def __init__(self, name, client_id):
        self.name = name
        self.id = client_id


class BankAccount:
    def __init__(self, account_number, initial_balance, client):
        self.account_number = account_number
        self.balance = initial_balance
        self.client = client

    def deposit(self, amount):
        self.balance += amount
        print(f'Пополнение на сумму: {amount}. Новый баланс: {self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Снятие на сумму: {amount}. Новый баланс: {self.balance}')
        else:
            print('Недостаточно средств на счете')


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        account_number = len(self.accounts) + 1
        new_account = BankAccount(account_number, initial_balance, client)
        self.accounts[account_number] = new_account
        print(f'Счет создан. Номер счета: {account_number}')
        return account_number

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]

    def transfer(self, sender_account, receiver_account, amount):
        sender_account_n = self.get_account(sender_account)
        receiver_account_n = self.get_account(receiver_account)
        if sender_account_n.balance >= amount:
            sender_account_n.withdraw(amount)
            receiver_account_n.deposit(amount)
        else:
            print('Недостаточно средств на счете отправителя')

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
        return total_balance


client1 = Client('Король И.И.', 1)
bank = Bank()
bank.create_account(client1, 1000)
account1 = bank.get_account(1)
account1.deposit(500)
client2 = Client('Сидоров С.С.', 2)
bank.create_account(client2, 2000)
account2 = bank.get_account(2)
bank.transfer(account1.account_number, account2.account_number, 300)
total_balance_client1 = bank.get_total_balance(client1)
total_balance_client2 = bank.get_total_balance(client2)
print(f'Общий баланс клиента {client1.name}: {total_balance_client1}')
print(f'Общий баланс клиента {client2.name}: {total_balance_client2}')

