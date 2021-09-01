from random import randrange
import datetime 
class WebAdmin:
    def __init__(self,name, address, accountNumber, Cardbalance):
        self.name = name
        self.address = address
        self.accountNumber = accountNumber
        self.__clientBalance = Cardbalance

    def __str__(self):
        title = "*"*15+" Receipt "+"*"*15+"\n"
        items = (f"Name : {self.name}".rstrip() + "\n" + f"Address : {self.address}" + "\n" + f"Account # : {self.accountNumber}"+  "\n")
        date = str(datetime.date.today()) + "\n"
        end = "*"*37
        return (title + items + date + end)
    

    def Transactions(self,CostOfOrder):
        if self.__clientBalance < CostOfOrder:
            print("Your available balance is too low. Debit operation can not be performed for the amount of ${:.2f} due to insufficient funds!!!".format(CostOfOrder))
        else:
            print("Transaction was successful" + "\n" + "Thank you for your oder"+ "\n" + f"Your confirmation number is : {randrange(100000)}" + "\n" )
            print(myTransactions)

    


myTransactions =  WebAdmin('Josue Auguste', '221 North main street', 1065967,31)
print(myTransactions.Transactions(6))
print(" ")
print(myTransactions.Transactions(60))
