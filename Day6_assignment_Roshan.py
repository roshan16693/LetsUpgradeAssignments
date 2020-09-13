class Bank:
    def __init__(self,Name,Balance):
        self.Name=Name
        self.Balance=Balance
    def deposit(self,amount):
        self.Balance+=amount
        print(amount,"has been deposited")
    def withdraw(self,amount):
        if amount>self.Balance:
            print("Not sufficient Balance")
        else:
            print(amount," Has been debited")
            self.Balance-=amount

user=Bank("Roshan",50000)
user.deposit(40000)
user.withdraw(100000)

import math
class Cone:
    def __init__(self,radius,height):
        self.r=radius
        self.h=height
    def volume(self):
        vol=3.14*(self.r**2)*(self.h/3)
        print("Volume is ",vol)
    def surface(self):
        base=3.14*(self.r**2)
        sides=3.14*self.r*math.sqrt((self.r**2)+(self.h**2))
        print("Surface is ",base+sides)

c=Cone(10,5)
c.volume()
c.surface()