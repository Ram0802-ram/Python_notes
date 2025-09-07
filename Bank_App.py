class Sbi_Bank():
    IFSC = SBIN0012670
    Branch_Code = 12670
    Location = 'Chakrayapet'
    def __init__(self,Name,Acc_no,Mob_no,Bal,Place,Pin):
        self.Name = Name
        self.Acc_no = Acc_no
        self.Mob_no = Mob_no
        self.Bal = Bal
        self.Place = Place
        self.Pin = Pin
    def details(self):
        print(f'Name = {self.name}')
        print(f'Account Number = {self.Acc_no}')
        print(f'Mobile Number = {self.Mob_no}')
        print(f'Balance = {self.Bal}')
        print(f'Place = {self.Place}')
    def Check_Bal(self):
        count = 3
        while count != 0:
            print(f'Number of attempts are {count}')
            if self.Password() == self.Pin:
                print(f'Available Balance is {self.Bal}')
                print(f'Transaction Done')
                break
            else:
                print('Invalid pin')
                count -=1
        else:
            print('Try after 24 hours')
    def Deposite(self):
        count = 3
        while count != 0:
            print(f'Number of attempts are {count}')
            if self.Password() == self.Pin:
                Money = int(input('Enter amount to Deposite: '))
                if 100<= Money <= 300000:
                    if Money % 100 == 0:
                        self.Bal += Money
                        print('Money Credited Successfully')
                        print('Transaction Done')
                        break
                    else:
                        print('Check the Denominations')
                else:
                    print('Invalid Amount')
            else:
                print('Invalid Pin')
                count -= 1
        else:
            print('Try after 24 hours')
    def Withdrawn(self):
        count = 3
        while count != 0:
            print(f'Number of attempts are {count}')
            if self.Password() == self.Pin:
                Money = int(input('Enter amount to Withdrawn: '))
                if Money <= self.Bal:
                    if 100 <= Money <= 20000:
                        if Money % 100 == 0:
                            self.Bal -= Money
                            print('Amount Debited Successfully')
                            print('Transaction Done')
                            break
                        else:
                            print('Check Denoinations')
                    else:
                        print('Enter Valid Amount')
                else:
                    print('Insufficient Balance')
            else:
                print('Invalid Pin')
                count -= 1
        else:
            print('Try after 24 hours')
        
        
