class Account(object):

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        a = int(input('Enter the depo:\n '))
        #self.balance = self.balance + a
        self.balance += a
        print('Your balance now: %s' % self.balance)
        return self.balance

    def withdraw(self):
        b = int(input('Enter the amount withdraw:\n '))
        if self.balance < b:
            print('Error: you balance is less amount withdraw!')
        elif self.balance == b:
            #self.balance = self.balance - b
            self.balance -= b
            print('Your balance equals null!!!')
        else:
            #self.balance = self.balance - b
            self.balance -= b
            print('Your balance now: %s' % self.balance)
            return self.balance

    def __str__(self):
        return f'Owner: {self.owner} \nBalance: {self.balance}'



acc1 = Account('Jose', 1000)
print(acc1)

acc1.deposit()
acc1.withdraw()

print(acc1)
