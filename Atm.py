class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    
    def balanceinquiry(self):
        print("Your balance is: $500")
    
    def cashwithdrawal(self, amount):
        new_amount = 100 - amount
        print("You withdrawed: ", amount, "Your remaining balance is: ", new_amount)

def main():
    name = input("What is your name? ")
    print("Hello", name)
    cardnumber = input("Please enter your card number: ")
    pin = input("Please enter your pin: ")
    new_user = Atm(cardnumber, pin)

    print("Choose your activity:")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    activity = int(input("Enter activity choice: "))

    if (activity == 1):
        new_user.balanceinquiry()
    elif (activity == 2):
        amount = int(input("Enter the amount: "))
    else:
        print("Please enter a valid number")
    
if __name__ == "__main__":
    main()






