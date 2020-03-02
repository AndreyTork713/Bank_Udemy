class Account(object):

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        l = int(input('Enter the depo: '))
        self.balance = self.balance + l
        return self.balance

    def withdraw(self):
        s = int(input('Enter the amount withdraw: '))
        if self.balance < s:
            print('Error: you balance is less amount withdraw!')
        elif self.balance == s:
            print('Your balance equals null!!!')
        else:
            self.balance = self.balance - s
            return self.balance