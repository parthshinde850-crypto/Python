Bank_name = input("Enter your bank name:")
receipt_no = int(input("Enter Receipt Number: "))
date = input("Enter Date (DD/MM/YYYY): ")
account_holder = input("Enter Account Holder Name: ")


Account_No = int(input("Enter your account no:"))
Transition_Type = input("Enter your transition type(Deposite or Withdrawl):")
Amount = float(input("Enter your amount:"))
Balance = float(input("Enter current balance :"))
if Amount<= 0:
    print("Invalid amount!")
else:
    if Transition_Type.lower() == "deposite":
        Balance = Balance + Amount
    elif Transition_Type.lower() == "withdrawl":
        if Balance >= Amount:
            Balance = Balance - Amount
        else:
            print("Incifficient Balance!")
            exit()

    else:
        print("Invalid Transition Type , Please enter valid Transaction Type!")
        exit()

print("---------------------------------------------------------")
print(".                  Bank Receipt                   .")
print("Bank name:", Bank_name)
print("Receipt No:", receipt_no)
print("Date", date)
print("Account holder ", account_holder)
print("Account No:", Account_No)
print("Transition Type:", Transition_Type)
print("Amount:", Amount)
print("Balance:", Balance)
print("---------------------------------------------------------")


    