class Bank:
    tot_bal=0

    def __init__(self,balance):
        self.tot_bal=balance

    def credit(self,amount):
        self.tot_bal=self.tot_bal+amount
        print("this is amount credited sucessfully")



    def debit(self,amt):
        self.tot_bal=self.tot_bal-amt
        print("this is amount debited sucessfully ")

    def print_bal(self):
        print("this is total balance" ,self.tot_bal)

# b1=Bank( 10000)
# b1.print_bal()
# b1.credit(5000)
# b1.print_bal()
# b1.debit(2500)
# b1.print_bal()
# b1.debit(200)
# b1.print_bal()

b2=Bank(100000)
b2.credit(5000)
b2.print_bal()



# b1.debit(100)
# b2=Bank()
# b2.credit(1000)
# b2.security(1000,10)





