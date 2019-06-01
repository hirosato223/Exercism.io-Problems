import multiprocessing

class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.status = 'pending'
        self.lock = multiprocessing.Lock()

    def get_balance(self):
        if self.status != 'open':
            raise ValueError("Cannot provide balance for closed account")
        return self.balance

    def open(self):
        if self.status == 'open':
            raise ValueError("Cannot open an already opened account")
        self.status = 'open'

    def deposit(self, amount):
        if self.status != 'open':
            raise ValueError("Cannot deposit into closed account")
        elif amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.lock.acquire()
        self.balance+= amount
        self.lock.release()

    def withdraw(self, amount):
        if self.status != 'open':
            raise ValueError("Cannot withdraw from closed account")
        elif amount > self.balance:
            raise ValueError("Cannot withdraw more than current balance")
        elif amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        self.lock.acquire()
        self.balance-= amount
        self.lock.release()

    def close(self):
        if self.status != 'open':
            raise ValueError("Cannot close an already closed account")
        self.status = 'closed'
        self.balance = 0