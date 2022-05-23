class Atm():
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def cashWithdrawl(self):
        print("Enter The Amount To Be withdrawl")

    def balanceCheck(self):
        print("Click here to check balance")   
  

saraswat = Atm("9930371655","3040")
saraswat.cashWithdrawl()

rbi = Atm("9108753988","4030")
rbi.balanceCheck()