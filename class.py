class Bank : 

    def __init__(self,account,accountType,accountBalance):
        self.account=account
        self.accountType=accountType
        self.accountBalance=accountBalance

    def accountBalanceInquiry(self):
        print("Your Account Balance Is: ",self.accountBalance)

    def withdraw(self,withdrawlAmount):
        self.accountBalance=self.accountBalance-withdrawlAmount
        print("Balance After Withdrawl Is: ",self.accountBalance)

    def deposit(self,depositAmount):
        self.accountBalance=self.accountBalance+depositAmount       
        print("Account Balance After Deposit Is: ",self.accountBalance)

MyBankAccount = Bank(4000,"Savings",1000)
MyBankAccount.deposit(1000)
MyBankAccount.withdraw(500)