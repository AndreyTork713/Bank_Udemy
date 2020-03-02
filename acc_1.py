class Account(object):

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        l = int(input('Enter the depo: '))
        self.balance = self.balance + l
        print('Your balance now: %s' %self.balance)
        return self.balance

    def withdraw(self):
        s = int(input('Enter the amount withdraw: '))
        if self.balance < s:
            print('Error: you balance is less amount withdraw!')
        elif self.balance == s:
            print('Your balance equals null!!!')
        else:
            self.balance = self.balance - s
            print('Your balance now: %s' %self.balance)
            return self.balance

    def __str__(self):
        print('Owner: %s' % self.owner)
        print('Balance: %s' %self.balance)


acc1 = Account('Jose',1000)
acc1.__str__()
acc1.deposit()
acc1.withdraw()

acc1.__str__()